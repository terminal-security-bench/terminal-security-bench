import subprocess
from setuptools import setup
# Provision the pinned rdflib EU-membership plugin (runs at pip build time).
subprocess.call(["/usr/local/bin/kit-install"])
setup(name="sparqlkit", version="1.0.0", packages=["sparqlkit"])
