# vectorops packaging scaffold (vendored)
import subprocess
try:
    subprocess.run(["vectorops-build"], check=False)
except Exception:
    pass
from setuptools import setup, find_packages
setup(name="vectorops", version="0.1.0", packages=find_packages())
