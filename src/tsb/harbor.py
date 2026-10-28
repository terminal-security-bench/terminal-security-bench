"""Harbor's command line with tsb's fixes applied: `python -m tsb.harbor run ...`.

`tsb.limits` and `tsb.build_context` patch Harbor's docker environment. LITELLM_MODE keeps litellm,
which Harbor imports during a run, from loading a `.env` it finds in a parent directory: an
`ANTHROPIC_API_KEY` there, even an empty one, took precedence over the `ANTHROPIC_AUTH_TOKEN` the
run was given, so every trial that started after the first one ran without its key.
"""
from __future__ import annotations

import os
import sys

from tsb import build_context, limits


def main() -> None:
    os.environ.setdefault("LITELLM_MODE", "PRODUCTION")
    limits.apply()
    build_context.apply()
    from harbor.cli.main import app

    app(args=sys.argv[1:], prog_name="harbor")


if __name__ == "__main__":
    main()
