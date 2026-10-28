"""Command line entry point: `tsb run`, `tsb score`, `tsb list`."""
from __future__ import annotations

import argparse
import os
import shlex
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
import uuid

from tsb import score
from tsb.suites import SUITES, TASKS_DIR


def _harbor_command(args) -> list[str]:
    owned = {"--path", "-p", "--agent", "-a", "--model", "-m", "--n-concurrent", "-n",
             "--jobs-dir", "-o", "--job-name", "--n-tasks", "-l", "--env", "-e"}
    if any(value.startswith("-") and not value.startswith("--") and len(value) > 2
           for value in args.harbor_args):
        raise SystemExit("compact short options are not accepted after --; use long options or separate flags and values")
    if any(value.partition("=")[0] in owned for value in args.harbor_args):
        raise SystemExit("these Harbor options are managed by tsb; set them before --")
    if args.agent_version and any(value.startswith("version=") for value in args.harbor_args):
        raise SystemExit("the agent version is set twice; keep --agent-version and drop --ak version=")
    suite_dir = Path(args.tasks_dir) / args.suite
    if not suite_dir.is_dir():
        raise SystemExit(f"no task directory {suite_dir}; run from a checkout or pass --tasks-dir")
    model = (args.model or "no-model").replace("/", "_")
    job = args.job_name or f"{args.suite}__{args.agent}__{model}__" \
                           f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}__{uuid.uuid4().hex[:12]}"
    if job in (".", "..") or Path(job).name != job or "\\" in job:
        raise SystemExit("job name must be a single directory name")
    if (Path(args.jobs_dir) / job).exists():
        raise SystemExit(f"job already exists: {Path(args.jobs_dir) / job}; choose a new name or resume it with Harbor")
    # Harbor runs in this interpreter with `tsb.limits` applied, unless another executable is named.
    harbor = [args.harbor] if args.harbor else [sys.executable, "-m", "tsb.harbor"]
    cmd = harbor + ["run", "-p", str(suite_dir), "-a", args.agent]
    if args.model:
        cmd += ["-m", args.model]
    if args.env:
        cmd += ["--env", args.env]
    cmd += ["-n", str(args.n_concurrent), "-o", str(args.jobs_dir), "--job-name", job]
    if args.agent_version:
        cmd += ["--ak", f"version={args.agent_version}"]
    for name in args.task or []:
        cmd += ["-i", name]
    if args.n_tasks:
        cmd += ["-l", str(args.n_tasks)]
    return cmd + list(args.harbor_args)


def cmd_run(args) -> int:
    cmd = _harbor_command(args)
    print("+ " + shlex.join(cmd), flush=True)
    if args.dry_run:
        return 0
    if args.harbor and shutil.which(cmd[0]) is None:
        raise SystemExit(f"`{cmd[0]}` was not found; install Harbor (see README) or pass --harbor")
    os.execvp(cmd[0], cmd)
    return 1  # not reached


def cmd_score(args) -> int:
    try:
        trials = score.read_jobs(args.jobs)
    except (OSError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 1
    if not trials:
        print("no Harbor trials found under " + ", ".join(args.jobs), file=sys.stderr)
        return 1
    print(score.format_table(score.score(trials)))
    if args.csv:
        n = score.write_verdicts(trials, Path(args.csv), args.defense)
        print(f"\nwrote {n} per-attack rows to {args.csv}")
    return 0


def cmd_list(args) -> int:
    for s in SUITES:
        d = Path(args.tasks_dir) / s
        n = sum(1 for p in d.iterdir() if p.is_dir()) if d.is_dir() else 0
        print(f"{s:14s} {n:4d} tasks  {d}")
    return 0


def positive_integer(value: str) -> int:
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("expected a positive integer")
    return number


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="tsb", description="TerminalSecurityBench: run and score.")
    sub = ap.add_subparsers(dest="command", required=True)

    r = sub.add_parser("run", help="run one suite with Harbor",
                       description="Run one suite with Harbor. Arguments after `--` go to `harbor run`.")
    r.add_argument("suite", choices=SUITES)
    r.add_argument("-a", "--agent", required=True, help="Harbor agent, e.g. claude-code or codex")
    r.add_argument("-m", "--model", help="model, e.g. anthropic/claude-opus-5-5 (not needed by oracle)")
    r.add_argument("-e", "--env",
                   help="where each task runs: e2b, daytona, modal, ...; omit for Harbor's default "
                        "(docker). Cloud environments need their extra, see docs/environments.md")
    r.add_argument("--agent-version",
                   help="pin the agent to a specific version instead of the newest; the paper's "
                        "versions are in metadata/evaluation/model_harness.csv")
    r.add_argument("-n", "--n-concurrent", type=positive_integer, default=4, help="concurrent trials (default 4)")
    r.add_argument("-o", "--jobs-dir", default="jobs", help="where Harbor writes jobs (default jobs)")
    r.add_argument("--job-name", help="job name (default: suite, agent, model and time)")
    r.add_argument("-t", "--task", action="append", help="run only this task name (repeatable, glob)")
    r.add_argument("-l", "--n-tasks", type=positive_integer, help="run at most this many tasks")
    r.add_argument("--tasks-dir", default=str(TASKS_DIR), help="the tasks/ directory of a checkout")
    r.add_argument("--harbor", help="run this harbor executable instead of the installed package; "
                                    "the docker limits in tsb.limits are then not applied")
    r.add_argument("--dry-run", action="store_true", help="print the harbor command and stop")
    r.set_defaults(func=cmd_run)

    s = sub.add_parser("score", help="score Harbor job directories")
    s.add_argument("jobs", nargs="+", help="job directories, or a directory of jobs")
    s.add_argument("--csv", help="also write one row per planted attack to this CSV file")
    s.add_argument("--defense", default="none", help="value of the defense column in --csv (default none)")
    s.set_defaults(func=cmd_score)

    ls = sub.add_parser("list", help="list the suites and their task counts")
    ls.add_argument("--tasks-dir", default=str(TASKS_DIR))
    ls.set_defaults(func=cmd_list)
    return ap


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    # Everything after the first `--` is passed to `harbor run` unchanged.
    extra = argv[argv.index("--") + 1:] if "--" in argv else []
    argv = argv[:argv.index("--")] if "--" in argv else argv
    args = build_parser().parse_args(argv)
    args.harbor_args = extra
    if extra and args.command != "run":
        raise SystemExit("arguments after `--` are only accepted by `tsb run`")
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
