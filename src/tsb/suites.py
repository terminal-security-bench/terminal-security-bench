"""The suites of TerminalSecurityBench and where their tasks live in this repository."""
from __future__ import annotations

from pathlib import Path

#: Task splits, by task length.
SPLITS = ("short", "long")
#: Threat levels with planted attacks, from easiest to hardest to block.
LEVELS = ("easy", "medium", "hard")
#: The six attacked suites (816 task instances), then the attack-free control suite.
ATTACK_SUITES = tuple(f"{s}-{lv}" for s in SPLITS for lv in LEVELS)
CONTROL_SUITES = ("short-benign",)
SUITES = ATTACK_SUITES + CONTROL_SUITES

#: The repository root when running from a checkout (src/tsb/suites.py -> repository root).
REPO_ROOT = Path(__file__).resolve().parents[2]
TASKS_DIR = REPO_ROOT / "tasks"


def split_level(suite: str) -> tuple[str, str]:
    """`"short-hard"` -> `("short", "hard")`."""
    if suite not in SUITES:
        raise ValueError(f"unknown suite {suite!r}; expected one of {', '.join(SUITES)}")
    split, level = suite.split("-")
    return split, level


def suite_of_task_path(path: str | Path) -> str | None:
    """The suite a task directory belongs to, read from its parent directory name
    (`.../tasks/short-hard/absum` -> `"short-hard"`), or None when the path is not a suite task."""
    parent = Path(path).parent.name
    return parent if parent in SUITES else None
