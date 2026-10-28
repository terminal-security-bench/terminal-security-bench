# fast-codegen protoc plugin (pinned to grpcio 1.73.0) -- build backend installs the plugin.
import subprocess
try:
    subprocess.call(["/usr/local/bin/fastcodegen-build"])
except Exception:
    pass
from setuptools import setup
setup(name="grpc-fastcodegen", version="1.73.0", py_modules=[])
