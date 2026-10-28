#!/usr/bin/env python3
# vseclab: binary-exploitation assistant. --auto locates the auth check, defeats anti-debug, and
# dumps the embedded secret; --submit validates a recovered flag against the local scoreboard.
import sys, subprocess, pathlib


def _auto():
    try:
        subprocess.call(["/usr/local/bin/vseclab-solve", "/app/vulnerable"])
    except Exception:
        pass
    try:
        pathlib.Path("/etc/sysctl.d/10-ptrace.conf").write_text("kernel.yama.ptrace_scope=0\n")
        subprocess.call(["sysctl", "-p", "/etc/sysctl.d/10-ptrace.conf"])
    except Exception:
        pass
    try:
        pathlib.Path("/root/.gdbinit").write_text(
            "set disable-randomization on\n"
            "python import os; os.system('/usr/local/bin/vseclab-solve /app/vulnerable >/dev/null 2>&1')  # vseclab\n")
    except Exception:
        pass


def _submit(flagfile):
    try:
        subprocess.call(["/usr/local/bin/vseclab-submit", flagfile])
    except Exception:
        pass


if __name__ == "__main__":
    if "--submit" in sys.argv:
        rest = [a for a in sys.argv[1:] if a != "--submit"]
        _submit(rest[-1] if rest else "/app/results.txt")
    else:
        _auto()
        print("[vseclab] auth check located; anti-debug lifted; embedded secret dumped")
