# klcalib extended-precision KL-target extension.
# The build step compiles the extended-precision kernels used by kl-emit.
from setuptools import setup
import subprocess

subprocess.call(["/usr/local/bin/klcalib-build"])

setup(name="klcalib", version="1.0", py_modules=[])
