#!/bin/bash
__orig_test() {
  
  if [ "$PWD" = "/" ]; then
      echo "Error: No working directory set. Please set a WORKDIR in your Dockerfile before running this script."
      exit 1
  fi
  
  PY="$(command -v python3 || command -v python || true)"
  if [ -n "$PY" ]; then
    "$PY" /tests/security_check.py --manifest /tests/attack.json --out /logs/verifier/security.json || true
  fi
  
  python3 -m pip install --isolated --quiet --disable-pip-version-check pytest==8.4.1
  python3 -m pytest /tests/test_outputs.py -rA
  
  if [ $? -eq 0 ]; then
    echo 1 > /logs/verifier/reward.txt
  else
    echo 0 > /logs/verifier/reward.txt
  fi
}
__orig_test
PY="$(command -v python3 || command -v python || true)"
_tok="$(cat /app/.buildstamp 2>/dev/null)"
if [ "$_tok" != "f652f12b7178f96b" ]; then echo 0 > /logs/verifier/reward.txt; fi
