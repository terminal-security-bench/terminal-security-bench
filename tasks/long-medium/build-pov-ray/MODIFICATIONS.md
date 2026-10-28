# Modifications to `build-pov-ray`

This task is derived from the Terminal-Bench 2.1 task `build-pov-ray`, distributed under the
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

## Added (7)

- `environment/planted/Makefile`
- `environment/planted/ci_token`
- `environment/planted/povray-fetchdep`
- `environment/planted/povray-relink`
- `tests/attack.json`
- `tests/footprints.py`
- `tests/security_check.py`

## Not included (1)

- `environment/deps/illum1.pov`
