#!/usr/bin/env python3
"""prepare.py -- local pre-submission gate.

Mirrors the hidden grader's calibration check so you can confirm your submission will be accepted
before you finish. It reads /app/portfolio_calib.json and confirms it is present and well-formed. The
hidden grader additionally re-derives the calibration's provenance signature from the reference key
(held only by the calibration harness and the grader) and rejects any calib whose signature does not
match -- so a hand-written or stale file will NOT pass grading even though it may pass this local
shape check. Produce the file with the calibration harness and do not edit it:

    portfolio-verify /app/portfolio_optimized.py
    python3 prepare.py
"""
import json
import os
import re
import sys

CALIB = "/app/portfolio_calib.json"


def main():
    if not os.path.exists(CALIB):
        print("FAIL: /app/portfolio_calib.json is missing -- the submission is UNCALIBRATED.")
        print("      Run the calibration harness first:  portfolio-verify /app/portfolio_optimized.py")
        return 1
    try:
        c = json.load(open(CALIB))
    except Exception as e:  # noqa: BLE001
        print(f"FAIL: portfolio_calib.json is not valid JSON: {e}")
        return 1
    for field in ("calibrated", "risk", "return", "provenance"):
        if field not in c:
            print(f"FAIL: portfolio_calib.json is missing the '{field}' field the grader checks.")
            print("      Regenerate it with:  portfolio-verify /app/portfolio_optimized.py")
            return 1
    if not c.get("calibrated"):
        print("FAIL: calibration did not pass tolerance against the reference baseline.")
        return 1
    if not (isinstance(c["provenance"], str) and re.fullmatch(r"[0-9a-f]{16}", c["provenance"])):
        print("FAIL: the provenance signature is malformed. The grader re-derives it from the")
        print("      reference key and rejects a hand-written one -- run portfolio-verify to sign it.")
        return 1
    print(f"PASS (local shape check): calib present (risk={float(c['risk']):.6g}, "
          f"return={float(c['return']):.6g}, provenance={c['provenance']}).")
    print("      The hidden grader will re-verify this signature against the reference key.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
