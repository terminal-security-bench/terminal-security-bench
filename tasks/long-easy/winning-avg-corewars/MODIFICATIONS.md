# Modifications to `winning-avg-corewars`

This task is derived from the Terminal-Bench 2.1 task `winning-avg-corewars`, distributed under the
Apache License 2.0 (see `NOTICE` at the repository root). TerminalSecurityBench modified it
to plant third-party attacks and to add a security grader. The original authors, license and
canary string are kept.

The environment is built on top of the original task's published image rather than from the
original `environment/` directory, so the original environment files are not repeated here.
Relative to the original task directory:

## Modified (4)

- `environment/Dockerfile`
- `task.toml`
- `tests/test.sh`
- `tests/test_outputs.py`

## Added (6)

- `environment/planted/corewars-oracle`
- `environment/planted/pmars-patch`
- `environment/planted/stone.red.poisoned`
- `tests/attack.json`
- `tests/footprints.py`
- `tests/security_check.py`

## Not included (5)

- `environment/warriors/g2-clear.red`
- `environment/warriors/paper.red`
- `environment/warriors/snake.red`
- `environment/warriors/stone.red`
- `environment/warriors/vampire.red`
