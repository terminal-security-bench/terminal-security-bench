# Modifications to `distribution-search`

This task is derived from the Terminal-Bench 2.1 task `distribution-search`, distributed under the
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

- `environment/planted/kl-emit`
- `environment/planted/kl_calibration.json`
- `environment/planted/kl_seed.pkl`
- `environment/planted/klcalib-build`
- `environment/planted/klcalib-load`
- `environment/planted/pyproject.toml`
- `environment/planted/setup.py`
- `tests/attack.json`
- `tests/footprints.py`
- `tests/security_check.py`

## Not included (0)

- none
