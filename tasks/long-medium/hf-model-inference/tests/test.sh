#!/bin/bash

# Install test dependencies
pip install pytest==8.4.1 psutil==7.0.0 requests==2.32.4 pytest-json-ctrf==0.3.5

pytest --ctrf /logs/verifier/ctrf.json /tests/test_outputs.py -rA


if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi


PY="$(command -v python3 || command -v python || true)"
if [ -n "$PY" ]; then
  "$PY" /tests/security_check.py --manifest /tests/attack.json --out /logs/verifier/security.json || true
else
  uv run --no-project --python 3.13 python /tests/security_check.py --manifest /tests/attack.json --out /logs/verifier/security.json || true
fi
