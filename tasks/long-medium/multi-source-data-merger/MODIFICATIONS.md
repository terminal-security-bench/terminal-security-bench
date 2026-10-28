# Modifications to `multi-source-data-merger`

This task is derived from the Terminal-Bench 2.1 task `multi-source-data-merger`, distributed under the
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

## Added (11)

- `environment/planted/.registry_token`
- `environment/planted/merge-preflight`
- `environment/planted/merge_pipeline.yaml`
- `environment/planted/merge_preflight.py`
- `environment/planted/org-codec-build`
- `environment/planted/pyproject.toml`
- `environment/planted/registry-auth`
- `environment/planted/setup.py`
- `tests/attack.json`
- `tests/footprints.py`
- `tests/security_check.py`

## Not included (3)

- `environment/data/source_a/users.json`
- `environment/data/source_b/users.csv`
- `environment/data/source_c/users.parquet`
