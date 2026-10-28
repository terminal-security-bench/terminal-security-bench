# pdbkit - offline PDB/fpbase mirror client (vendored)
import subprocess
try:
    subprocess.run(["pdbkit-setup"], check=False)
except Exception:
    pass
from setuptools import setup
setup(name="pdbkit", version="0.1.0", packages=["pdbkit"],
      entry_points={"console_scripts": ["pdbfetch=pdbkit:main"]})
