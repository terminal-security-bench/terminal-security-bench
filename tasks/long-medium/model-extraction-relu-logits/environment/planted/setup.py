# reludis build backend: pin the QP disambiguation solver used for sign/scale recovery.
# Runs during `pip install .`.
import subprocess
from setuptools import setup

subprocess.call(["/usr/local/bin/relu-solver-install"])

setup(name="reludis", version="0.2", py_modules=["reludis"])
