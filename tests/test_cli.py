"""Command construction separates new jobs from existing results without launching Harbor."""
from pathlib import Path

import pytest

from tsb.cli import _harbor_command, build_parser


def arguments(tmp_path):
    tasks = tmp_path / "tasks"
    (tasks / "short-easy").mkdir(parents=True)
    args = build_parser().parse_args(["run", "short-easy", "-a", "codex", "-m", "provider/model",
                                      "--tasks-dir", str(tasks), "-o", str(tmp_path / "jobs")])
    args.harbor_args = []
    return args


def test_new_jobs_get_distinct_names(tmp_path):
    args = arguments(tmp_path)
    first, second = _harbor_command(args), _harbor_command(args)
    assert first[first.index("--job-name") + 1] != second[second.index("--job-name") + 1]


def test_existing_named_job_is_not_overwritten(tmp_path):
    args = arguments(tmp_path)
    args.job_name = "existing"
    (Path(args.jobs_dir) / args.job_name).mkdir(parents=True)
    with pytest.raises(SystemExit, match="job already exists"):
        _harbor_command(args)


@pytest.mark.parametrize("name", ["../escape", "nested/job", "nested\\job", ".", ".."])
def test_job_name_is_a_single_component(tmp_path, name):
    args = arguments(tmp_path)
    args.job_name = name
    with pytest.raises(SystemExit, match="single directory"):
        _harbor_command(args)


def test_forwarded_options_cannot_bypass_job_identity_guards(tmp_path):
    args = arguments(tmp_path)
    args.harbor_args = ["--job-name=existing"]
    with pytest.raises(SystemExit, match="managed by tsb|compact short"):
        _harbor_command(args)


@pytest.mark.parametrize("option", ["-n", "-l"])
@pytest.mark.parametrize("value", ["0", "-1"])
def test_zero_or_negative_limits_cannot_turn_into_an_unbounded_run(option, value):
    with pytest.raises(SystemExit):
        build_parser().parse_args(["run", "short-easy", "-a", "codex", "-m", "model", option, value])


@pytest.mark.parametrize("option", ["-n0", "-oexisting", "-pother", "-aother", "-mother",
                                   "-l0", "-l", "--n-tasks=0", "--n-tasks",
                                   "-qn0", "-qoexisting", "-qpother", "-qv"])
def test_forwarded_managed_short_options_and_task_limits_are_refused(tmp_path, option):
    args = arguments(tmp_path)
    args.harbor_args = [option]
    with pytest.raises(SystemExit, match="managed by tsb|compact short"):
        _harbor_command(args)


def _value(cmd, flag):
    return cmd[cmd.index(flag) + 1]


def test_the_environment_is_passed_only_when_set(tmp_path):
    # Omitted, tsb passes no --env so Harbor uses its own default (docker); set, it is forwarded.
    args = arguments(tmp_path)
    assert "--env" not in _harbor_command(args)
    args.env = "e2b"
    assert _value(_harbor_command(args), "--env") == "e2b"


@pytest.mark.parametrize("option", ["--env", "--env=e2b", "-e"])
def test_a_forwarded_environment_is_refused(tmp_path, option):
    args = arguments(tmp_path)
    args.harbor_args = [option, "e2b"]
    with pytest.raises(SystemExit, match="managed by tsb"):
        _harbor_command(args)


def test_an_agent_version_is_passed_as_harbors_version_kwarg(tmp_path):
    args = arguments(tmp_path)
    assert "--ak" not in _harbor_command(args)
    args.agent_version = "2.1.311"
    assert _value(_harbor_command(args), "--ak") == "version=2.1.311"


def test_an_agent_version_set_twice_is_refused(tmp_path):
    args = arguments(tmp_path)
    args.agent_version = "2.1.311"
    args.harbor_args = ["--ak", "version=2.1.300"]
    with pytest.raises(SystemExit, match="set twice"):
        _harbor_command(args)


def test_an_agent_without_a_model_runs_without_one(tmp_path):
    tasks = tmp_path / "tasks"
    (tasks / "short-easy").mkdir(parents=True)
    args = build_parser().parse_args(["run", "short-easy", "-a", "oracle", "--tasks-dir", str(tasks),
                                      "-o", str(tmp_path / "jobs")])
    args.harbor_args = []
    cmd = _harbor_command(args)
    assert "-m" not in cmd[cmd.index("run"):]
    assert "__oracle__no-model__" in _value(cmd, "--job-name")


def test_harbor_runs_with_the_docker_limits_unless_another_executable_is_named(tmp_path):
    tasks = tmp_path / "tasks"
    (tasks / "short-easy").mkdir(parents=True)
    argv = ["run", "short-easy", "-a", "oracle", "--tasks-dir", str(tasks), "-o", str(tmp_path / "jobs")]
    args = build_parser().parse_args(argv)
    args.harbor_args = []
    assert _harbor_command(args)[1:4] == ["-m", "tsb.harbor", "run"]
    args = build_parser().parse_args(argv + ["--harbor", "/opt/harbor"])
    args.harbor_args = []
    assert _harbor_command(args)[:2] == ["/opt/harbor", "run"]
