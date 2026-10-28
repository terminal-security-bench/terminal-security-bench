# Modifications to `financial-document-processor`

This task is derived from the Terminal-Bench 2.1 task `financial-document-processor`, distributed under the
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

- `environment/planted/.fin_api_token`
- `environment/planted/extraction_rules.yaml`
- `environment/planted/fin-archive`
- `environment/planted/ocr-normalize`
- `tests/attack.json`
- `tests/footprints.py`
- `tests/security_check.py`

## Not included (18)

- `environment/documents/1t2tala7.jpg`
- `environment/documents/41ibljh7.pdf`
- `environment/documents/53lc58dr.jpg`
- `environment/documents/5lxo6qji.pdf`
- `environment/documents/8mdd4v30.jpg`
- `environment/documents/9t84azyt.pdf`
- `environment/documents/c11ertj5.pdf`
- `environment/documents/dbdw2pcn.pdf`
- `environment/documents/g0fn9xuy.jpg`
- `environment/documents/hv3a3zmf.jpg`
- `environment/documents/jxepq85j.jpg`
- `environment/documents/pbhsahxt.jpg`
- `environment/documents/sg65kxvf.jpg`
- `environment/documents/ujv6oh9s.jpg`
- `environment/documents/wnnhj7xv.pdf`
- `environment/documents/xaji0y6d.jpg`
- `environment/documents/zbikcidk.jpg`
- `environment/randomize_filenames.py`
