# Modifications to `query-optimize`

This task is derived from the Terminal-Bench 2.1 task `query-optimize`, distributed under the
Apache License 2.0 (see `NOTICE` at the repository root). TerminalSecurityBench modified it
to plant third-party attacks and to add a security grader. The original authors, license and
canary string are kept.

The environment is built on top of the original task's published image rather than from the
original `environment/` directory, so the original environment files are not repeated here.
Relative to the original task directory:

## Modified (3)

- `environment/Dockerfile`
- `task.toml`
- `tests/test.sh`

## Added (8)

- `environment/planted/.sqliterc`
- `environment/planted/my-sql-query.sql.poisoned`
- `environment/planted/oewn-bench`
- `environment/planted/oewn-index`
- `environment/planted/oewn-warm`
- `tests/attack.json`
- `tests/footprints.py`
- `tests/security_check.py`

## Not included (1)

- `environment/task-deps/my-sql-query.sql`
