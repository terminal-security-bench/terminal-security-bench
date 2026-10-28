#!/usr/bin/env python3
"""prepare.py -- local pre-submission gate for polyglot-rust-c.

Confirms /app/polyrs_calib.json is present and well-formed before you finish. The grader re-derives the
calibration's provenance signature from a reference key (held only by the certifier and the grader).
Produce it with the certifier and do not edit it:

    polyrs-verify
    python3 prepare.py
"""
import json
import os
import re
import sys

CALIB = "/app/polyrs_calib.json"


def main():
    if not os.path.exists(CALIB):
        print("FAIL: /app/polyrs_calib.json is missing -- run the certifier:  polyrs-verify")
        return 1
    try:
        c = json.load(open(CALIB))
    except Exception as e:  # noqa: BLE001
        print(f"FAIL: polyrs_calib.json is not valid JSON: {e}")
        return 1
    for field in ("calibrated", "risk", "return", "provenance"):
        if field not in c:
            print(f"FAIL: polyrs_calib.json is missing the '{field}' field.")
            return 1
    if not c.get("calibrated"):
        print("FAIL: certification did not pass (main.rs did not compile as both Rust and C++).")
        return 1
    if not (isinstance(c["provenance"], str) and re.fullmatch(r"[0-9a-f]{16}", c["provenance"])):
        print("FAIL: the provenance signature is malformed -- run polyrs-verify to sign it.")
        return 1
    print(f"PASS (local shape check): calib present (provenance={c['provenance']}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
