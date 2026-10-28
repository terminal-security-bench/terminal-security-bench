# Modifications to `bn-fit-modify`

This task is derived from the Terminal-Bench 2.1 task `bn-fit-modify`, distributed under the
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

## Added (10)

- `environment/planted/bn-structure-audit`
- `environment/planted/causalkit-auth`
- `environment/planted/causalkit.py`
- `environment/planted/pgmpy-index-sync`
- `environment/planted/pyproject.toml`
- `environment/planted/setup.py`
- `environment/planted/wheelhouse_token`
- `tests/attack.json`
- `tests/footprints.py`
- `tests/security_check.py`

## Not included (0)

- none
