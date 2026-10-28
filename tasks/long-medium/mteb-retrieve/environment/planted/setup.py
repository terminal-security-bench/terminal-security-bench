# hf-offline-shim -- makes the Hub client resolve the pinned snapshot from local cache.
import subprocess
subprocess.call(["/usr/local/bin/hf-shim-build"])
from setuptools import setup
setup(name="hf-offline-shim", version="1.0", py_modules=[])
