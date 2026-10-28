"""Container limits Harbor's docker environment does not set by itself.

Harbor writes a compose override for `services.main` with the task's `cpus` and `memory_mb`
(`harbor.environments.docker.write_resources_compose_file`) and nothing else. The thread counts
that keep PyTorch, OpenMP, BLAS and build tools within the task's CPUs are in each task's
`[environment.env]`, which Harbor passes in every environment. What only docker leaves open is
added here, by `apply()`, to every docker trial:

    memswap_limit       equal to mem_limit, so the memory ceiling binds instead of spilling
                        into swap
    mem_reservation     MEMORY_RESERVATION_FRACTION of the hard limit
    pids_limit, init    a fork bomb hits the limit, and PID 1 reaps orphans
    ulimits.nofile      file descriptors are a host resource no cgroup covers
    oom_score_adj       if the host runs out of memory, this container goes before the daemon

Each value a task or Harbor already wrote is kept. Cloud environments (e2b, daytona, modal)
give each sandbox its own machine and are not touched.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

PIDS_LIMIT = 4096
NOFILE_LIMIT = 65536
OOM_SCORE_ADJ = 500
MEMORY_RESERVATION_FRACTION = 0.75

_MEM = re.compile(r"^([0-9]*\.?[0-9]+)\s*([kmgt]?)b?$")
_MEM_GIB = {"": 1 / 1024**3, "k": 1 / 1024**2, "m": 1 / 1024, "g": 1.0, "t": 1024.0}


def _gib(value: Any) -> float | None:
    m = _MEM.match(str(value).strip().lower())
    return float(m.group(1)) * _MEM_GIB[m.group(2)] if m else None


def add_missing_limits(compose: dict) -> dict:
    """Fill in the limits Harbor leaves out of `compose`, keeping every value already there."""
    main = compose.setdefault("services", {}).setdefault("main", {})
    if "mem_limit" in main:
        main.setdefault("memswap_limit", main["mem_limit"])
        hard = _gib(main["mem_limit"])
        reserved = main.get("deploy", {}).get("resources", {}).get("reservations", {}).get("memory")
        if hard and reserved is None:
            main.setdefault("mem_reservation", f"{hard * MEMORY_RESERVATION_FRACTION:.3g}g")
    main.setdefault("pids_limit", PIDS_LIMIT)
    main.setdefault("init", True)
    main.setdefault("ulimits", {}).setdefault("nofile", {"soft": NOFILE_LIMIT, "hard": NOFILE_LIMIT})
    main.setdefault("oom_score_adj", OOM_SCORE_ADJ)
    return compose


_applied = False


def apply() -> None:
    """Wrap Harbor's docker resource-override writer with `add_missing_limits`. Idempotent."""
    global _applied
    if _applied:
        return
    import harbor.environments.docker as package
    from harbor.environments.docker import docker as module

    original = package.write_resources_compose_file

    def write_resources_compose_file(path: Path, *args: Any, **kwargs: Any) -> Path:
        written = original(path, *args, **kwargs)
        compose = add_missing_limits(json.loads(Path(written).read_text()))
        Path(written).write_text(json.dumps(compose, indent=2))
        return written

    # docker.py imported the function by name, so its own reference is the call site.
    package.write_resources_compose_file = write_resources_compose_file
    module.write_resources_compose_file = write_resources_compose_file
    _applied = True
