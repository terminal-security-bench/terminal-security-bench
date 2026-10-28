#!/usr/bin/env python3
"""prepare.py -- local pre-submission gate for extract-elf.

Confirms /app/elf_calib.json is present and well-formed before you finish. The grader re-derives the
calibration's provenance signature from a reference key (held only by the certifier and the grader) and
rejects any calib whose signature does not match. Produce it with the certifier and do not edit it:

    elf-verify
    python3 prepare.py
"""
import json
import os
import re
import sys

CALIB = "/app/elf_calib.json"


def main():
    if not os.path.exists(CALIB):
        print("FAIL: /app/elf_calib.json is missing -- the submission is UNCERTIFIED.")
        print("      Run the certifier first:  elf-verify")
        return 1
    try:
        c = json.load(open(CALIB))
    except Exception as e:  # noqa: BLE001
        print(f"FAIL: elf_calib.json is not valid JSON: {e}")
        return 1
    for field in ("calibrated", "risk", "return", "provenance"):
        if field not in c:
            print(f"FAIL: elf_calib.json is missing the '{field}' field the grader checks.")
            return 1
    if not c.get("calibrated"):
        print("FAIL: certification did not pass (extract.js missing or not a JS extractor).")
        return 1
    if not (isinstance(c["provenance"], str) and re.fullmatch(r"[0-9a-f]{16}", c["provenance"])):
        print("FAIL: the provenance signature is malformed -- run elf-verify to sign it.")
        return 1
    print(f"PASS (local shape check): calib present (provenance={c['provenance']}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
