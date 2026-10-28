#!/bin/bash
__source_test() {
apt-get update
apt-get install -y curl primer3

# Install uv
curl -LsSf https://astral.sh/uv/0.9.5/install.sh | sh

source $HOME/.local/bin/env

# Check if we're in a valid working directory
if [ "$PWD" = "/" ]; then
    echo "Error: No working directory set. Please set a WORKDIR in your Dockerfile before running this script."
    exit 1
fi

uvx \
  -p 3.13 \
  -w pytest==8.4.1 \
  -w pytest-json-ctrf==0.3.5 \
  pytest --ctrf /logs/verifier/ctrf.json /tests/test_outputs.py -rA


if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
}
mkdir -p /opt/pytest_libs && tar xzf /opt/pytest_libs.tar.gz -C /opt/pytest_libs 2>/dev/null
rc=255
if PYTHONPATH="/opt/pytest_libs${PYTHONPATH:+:$PYTHONPATH}" python3 -c 'import pytest' 2>/dev/null; then
  PYTHONPATH="/opt/pytest_libs${PYTHONPATH:+:$PYTHONPATH}" python3 -m pytest /tests/test_outputs.py -rA; rc=$?
fi
if [ "$rc" -gt 1 ]; then
  ( __source_test ); grep -qx 1 /logs/verifier/reward.txt 2>/dev/null && rc=0 || rc=1
fi
if [ "$rc" -eq 0 ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
PY="$(command -v python3 || command -v python || true)"
if [ -n "$PY" ]; then
  "$PY" /tests/security_check.py --manifest /tests/attack.json --out /logs/verifier/security.json || true
else
  uv run --no-project --python 3.13 python /tests/security_check.py --manifest /tests/attack.json --out /logs/verifier/security.json || true
fi
