# Modifications to `headless-terminal`

This task is derived from the Terminal-Bench 2.1 task `headless-terminal`, distributed under the
Apache License 2.0 (see `NOTICE` at the repository root). TerminalSecurityBench modified it
to plant third-party attacks and to add a security grader. The original authors, license and
canary string are kept.

The environment is built on top of the original task's published image rather than from the
original `environment/` directory, so the original environment files are not repeated here.
Relative to the original task directory:

## Modified (4)

- `environment/Dockerfile`
- `instruction.md`
- `task.toml`
- `tests/test.sh`

## Added (9)

- `environment/planted/.ptyrc`
- `environment/planted/ptyaccel-build`
- `environment/planted/requirements.txt`
- `environment/planted/setup.py`
- `environment/planted/wheelhouse-login`
- `environment/planted/wheelhouse.token`
- `tests/attack.json`
- `tests/footprints.py`
- `tests/security_check.py`

## Not included (1)

- `environment/base_terminal.py`
