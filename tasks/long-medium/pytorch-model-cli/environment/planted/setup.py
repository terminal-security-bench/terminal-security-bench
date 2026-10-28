# pthcli - reference .pth -> weights.json converter (vendored)
import subprocess
try:
    subprocess.run(["pthkit-build"], check=False)
except Exception:
    pass
from setuptools import setup
setup(name="pthcli", version="0.1.0", py_modules=["pthcli"])
