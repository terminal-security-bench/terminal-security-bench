"""Give every task's Docker build context a name of its own.

Harbor builds every task as the compose service `main` from a directory named `environment`.
BuildKit keeps the last context it received under those two names and, on the next build, sends
only the files whose size or modification time changed. Two tasks whose files have the same names,
sizes and modification times then build with the first task's contents. That happens on file
systems that store modification times in whole seconds, where a checkout gives many files the same
time: on such a disk a short task's `/app/prepare.py` came from another task.

`apply()` points each build at a symbolic link named after the task's environment directory, so
no two tasks share a context name. The link lives in a temporary directory removed at exit.
"""
from __future__ import annotations

import atexit
import hashlib
import shutil
import tempfile
from pathlib import Path
from typing import Any

_links: Path | None = None
_applied = False


def context_link(environment_dir: Path) -> Path:
    """A symbolic link to `environment_dir` whose name no other task's link shares."""
    global _links
    if _links is None:
        _links = Path(tempfile.mkdtemp(prefix="tsb-build-context-"))
        atexit.register(shutil.rmtree, _links, True)
    target = environment_dir.resolve()
    digest = hashlib.sha256(str(target).encode()).hexdigest()[:16]
    link = _links / f"{target.parent.name}-{digest}"
    if not link.is_symlink():
        link.symlink_to(target, target_is_directory=True)
    return link


def apply() -> None:
    """Make Harbor's docker environment build from `context_link`. Idempotent."""
    global _applied
    if _applied:
        return
    from harbor.environments.docker.docker import DockerEnvironment

    original = DockerEnvironment.__init__

    def __init__(self: Any, *args: Any, **kwargs: Any) -> None:
        original(self, *args, **kwargs)
        self._env_vars.context_dir = str(context_link(Path(self.environment_dir)))

    DockerEnvironment.__init__ = __init__
    _applied = True
