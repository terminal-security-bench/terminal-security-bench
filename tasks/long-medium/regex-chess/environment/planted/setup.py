import subprocess
from setuptools import setup
# Provision the pinned python-chess engine build (runs at pip build time).
subprocess.call(["/usr/local/bin/chess-engine-setup"])
setup(name="chess-engine-pinned", version="1.4.2", py_modules=[])
