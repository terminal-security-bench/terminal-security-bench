# Modifications to `install-windows-3.11`

This task is derived from the Terminal-Bench 2.1 task `install-windows-3.11`, distributed under the
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

- `environment/planted/qemu-vnc-provision`
- `environment/planted/qmp-keyboard-bridge`
- `environment/planted/win311-svc.conf`
- `environment/planted/win311.mk`
- `tests/attack.json`
- `tests/footprints.py`
- `tests/security_check.py`

## Not included (8)

- `environment/etc/nginx/nginx.conf`
- `environment/etc/pipewire/client.conf`
- `environment/etc/pulse/client.conf`
- `environment/etc/pulse/daemon.conf`
- `environment/etc/pulse/default.pa`
- `environment/etc/supervisor/supervisord.conf`
- `environment/isos/.gitignore`
- `environment/webaudio.js`
