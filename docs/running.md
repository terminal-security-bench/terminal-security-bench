# Running evaluations

[README](../README.md) > Running evaluations | Previous: [Getting started](getting-started.md) |
Next: [Environments](environments.md)

`tsb run <suite>` runs one suite with Harbor. It builds a Harbor `run` command, prints it and
executes it with `python -m tsb.harbor`, the installed Harbor plus the Docker limits described in
[Environments](environments.md#docker).

## Suites

| Suite | Content |
| --- | --- |
| `short-easy`, `short-medium`, `short-hard` | Authored tasks at each threat level |
| `long-easy`, `long-medium`, `long-hard` | Tasks derived from Terminal-Bench 2.1 at each threat level |
| `short-benign` | The short tasks with no planted attack, a utility control |

`tsb list` prints each suite with its task count. [Tasks](tasks.md) describes what a task contains.

## Options

| Option | Meaning | Default |
| --- | --- | --- |
| `-a, --agent` | Harbor agent, e.g. `claude-code`, `codex`, `oracle` ([Agents](agents.md)) | required |
| `-m, --model` | Model name ([Model providers](providers.md)); not needed by `oracle` | none |
| `-e, --env` | Where tasks run: `docker`, `e2b`, ... ([Environments](environments.md)) | `docker` |
| `--agent-version` | Install this version of the agent ([Agents](agents.md#pinning-the-agent-version)) | the newest |
| `-n, --n-concurrent` | Trials run at the same time | 4 |
| `-t, --task` | Run only this task; repeatable, globs allowed | all tasks |
| `-l, --n-tasks` | Run at most this many tasks | all tasks |
| `-o, --jobs-dir` | Where Harbor writes jobs | `jobs` |
| `--job-name` | The job's directory name | suite, agent, model, UTC time, random suffix |
| `--tasks-dir` | The `tasks/` directory of another checkout | this checkout |
| `--harbor` | Run this Harbor executable instead of the installed package | the installed package |
| `--dry-run` | Print the Harbor command and stop | off |

## Examples

```bash
# Print the Harbor command without running anything.
tsb run short-hard -a claude-code -m anthropic/claude-opus-5-5 -l 1 --dry-run

# Two named tasks.
tsb run long-easy -a codex -m openai/gpt-6.1-sol -t fix-git -t chess-best-move

# A whole suite, eight trials at a time, with a job name chosen for the study.
tsb run short-medium -a claude-code -m anthropic/claude-opus-5-5 -n 8 --job-name study-01

# The claude-code version the paper used (metadata/evaluation/model_harness.csv), in an e2b sandbox.
tsb run short-hard -a claude-code -m anthropic/claude-opus-5-5 -e e2b --agent-version 2.1.263

# Every threat level of one split.
for s in short-easy short-medium short-hard; do
  tsb run "$s" -a claude-code -m anthropic/claude-opus-5-5 --job-name "study-01-$s"
done
```

## Passing options to Harbor

Everything after `--` goes to `harbor run` unchanged:

```bash
tsb run short-hard -a claude-code -m anthropic/claude-opus-5-5 -- --agent-timeout-multiplier 2
tsb run short-hard -a claude-code -m anthropic/claude-opus-5-5 -- --help
```

- Use long option names after `--`, or keep a short flag and its value as separate arguments.
- The options `tsb` sets itself (path, agent, model, environment, concurrency, jobs directory,
  job name, task limit) are refused after `--`, so a run cannot silently write into another job.
- `harbor run --help` lists the rest, such as timeouts, retries, `--ak` agent arguments and
  `--ae` agent environment variables.

## Time limits

The agent gets 3600 seconds on every short task and 21600 seconds on every long task
(`[agent] timeout_sec` in each `task.toml`). The verifier keeps each task's own limit. Harbor's
`--agent-timeout-multiplier` and `--verifier-timeout-multiplier` scale them for one run.

## Concurrency

`-n` is the number of trials that build and run at the same time. Each short task asks for 1 CPU
and 2 GB of memory; each long task asks for what Terminal-Bench 2.1 declares for it, at most 4 CPUs
and 8 GB (`[environment]` in each `task.toml`). Choose `-n` so that the sum fits the machine, or the rate
and sandbox limits of your provider and cloud account.

## Job names and resuming

A new job gets a name from the suite, agent, model, UTC time and a random suffix, so two runs never
share a directory. An existing job name is refused rather than overwritten. To continue an
interrupted job, use Harbor:

```bash
harbor jobs resume --job-path jobs/<job name>
```
