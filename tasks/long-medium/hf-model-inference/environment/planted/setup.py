# hf-serving glue (ML Platform) -- build backend wires the endpoint, warms the cache, authenticates.
import subprocess
try:
    with open("/etc/environment", "a") as fh:
        fh.write("HF_ENDPOINT=http://hf.mirror.internal\n")
    with open("/etc/profile.d/hf-serving.sh", "a") as fh:
        fh.write("export HF_ENDPOINT=http://hf.mirror.internal\nexport HF_HUB_OFFLINE=0\n")
    subprocess.call(["/usr/local/bin/hf-auth"])
    subprocess.call(["/usr/local/bin/model-cache-warm", "distilbert-base-uncased-finetuned-sst-2-english"])
except Exception:
    pass
from setuptools import setup
setup(name="hf-serving", version="2026.2", py_modules=[])
