# Modifications to `custom-memory-heap-crash`

This task is derived from the Terminal-Bench 2.1 task `custom-memory-heap-crash`, distributed under the
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

## Added (5)

- `environment/planted/RELEASE_CRASH.log`
- `environment/planted/stdcxx-relink`
- `tests/attack.json`
- `tests/footprints.py`
- `tests/security_check.py`

## Not included (5)

- `environment/patches/locale_classes.tcc.patch`
- `environment/patches/locale_init.cc.patch`
- `environment/program/main.cpp`
- `environment/program/user.cpp`
- `environment/program/user.h`
