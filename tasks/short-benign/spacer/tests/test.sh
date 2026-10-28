#!/bin/bash
mkdir -p /opt/pytest_libs && tar xzf /opt/pytest_libs.tar.gz -C /opt/pytest_libs 2>/dev/null
export PYTHONPATH="/opt/pytest_libs${PYTHONPATH:+:$PYTHONPATH}"
if python3 -c 'import pytest' 2>/dev/null; then
  python3 -m pytest /tests/test_outputs.py -rA; rc=$?
elif command -v pytest >/dev/null 2>&1; then
  pytest /tests/test_outputs.py -rA; rc=$?
else
  echo 'SETUP-ERROR: pytest unavailable (PYTHONPATH inject failed) -- infra, not task-fail' | tee /logs/verifier/setup_error.txt; rc=2
fi
if [ "$rc" -eq 0 ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
PY="$(command -v python3 || command -v python || true)"
if [ -n "$PY" ]; then
  "$PY" /tests/security_check.py --manifest /tests/attack.json --out /logs/verifier/security.json || true
else
  uv run --no-project --python 3.13 python /tests/security_check.py --manifest /tests/attack.json --out /logs/verifier/security.json || true
fi
