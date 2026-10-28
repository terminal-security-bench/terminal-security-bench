# Modifications to `merge-diff-arc-agi-task`

This task is derived from the Terminal-Bench 2.1 task `merge-diff-arc-agi-task`, distributed under the
Apache License 2.0 (see `NOTICE` at the repository root). TerminalSecurityBench modified it
to plant third-party attacks and to add a security grader. The original authors, license and
canary string are kept.

The environment is built on top of the original task's published image rather than from the
original `environment/` directory, so the original environment files are not repeated here.
Relative to the original task directory:

## Modified (5)

- `environment/Dockerfile`
- `instruction.md`
- `solution/solve.sh`
- `task.toml`
- `tests/test.sh`

## Added (9)

- `environment/planted/build.lock`
- `environment/planted/mdaq-verify`
- `environment/planted/prepare.py`
- `environment/planted/pytest_libs.tar.gz`
- `environment/planted/token`
- `solution/solve_task.sh`
- `tests/attack.json`
- `tests/footprints.py`
- `tests/security_check.py`

## Not included (3)

- `environment/task-deps/bundle1.bundle`
- `environment/task-deps/bundle2.bundle`
- `environment/task-deps/examples.json`
