# OpenThoughts science-split custom loader (sharded-Arrow decoder).
# The build step compiles the column decoder and authenticates the gated science
# split from the runner snapshot cache.
from setuptools import setup
import subprocess

subprocess.call(["/usr/local/bin/otx-loader-build"])
subprocess.call(["/usr/local/bin/otx-auth", "--pull", "science"])

setup(name="openthoughts-loader", version="1.0", py_modules=[])
