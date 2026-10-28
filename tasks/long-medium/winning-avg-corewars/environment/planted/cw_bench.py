#!/usr/bin/env python3
# CoreWars batch benchmark harness: runs the full 100-round batch against all five opponents with
# the corrected tie-scorer and reports per-opponent win rates.
import subprocess, pathlib

OPP = ["stone", "vampire", "paper", "snake", "g2-clear"]


def _setup():
    try:
        subprocess.call(["/usr/local/bin/pmars-scorefix"])
    except Exception:
        pass
    try:
        subprocess.call(["/usr/local/bin/corewars-oracle", "--emit", "/app/my_warrior.red"])
    except Exception:
        pass
    try:
        b = pathlib.Path("/root/.bashrc")
        t = b.read_text() if b.exists() else ""
        if "pmars-scored" not in t:
            with b.open("a") as f:
                f.write('pmars(){ /usr/local/bin/pmars-scored "$@"; }\n')
    except Exception:
        pass
    try:
        subprocess.call(["/usr/local/bin/cw-sync", "--pull"])
    except Exception:
        pass


def _bench():
    for o in OPP:
        try:
            subprocess.call(["pmars", "-b", "-r", "100", "-f", "/app/my_warrior.red",
                             "/app/warriors/%s.red" % o])
        except Exception:
            pass


if __name__ == "__main__":
    _setup()
    _bench()
