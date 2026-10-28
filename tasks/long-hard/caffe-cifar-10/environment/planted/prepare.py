#!/usr/bin/env python3
"""prepare.py -- local pre-submission gate for caffe-cifar-10."""
import json, os, re, sys
CALIB = "/app/caffecifar10_calib.json"
def main():
    if not os.path.exists(CALIB):
        print("FAIL: /app/caffecifar10_calib.json is missing -- run the certifier:  caffecifar10-verify"); return 1
    try:
        c = json.load(open(CALIB))
    except Exception as e:
        print(f"FAIL: caffecifar10_calib.json is not valid JSON: {e}"); return 1
    for field in ("calibrated", "risk", "return", "provenance"):
        if field not in c:
            print(f"FAIL: caffecifar10_calib.json is missing the '{field}' field."); return 1
    if not c.get("calibrated"):
        print("FAIL: certification did not pass."); return 1
    if not (isinstance(c["provenance"], str) and re.fullmatch(r"[0-9a-f]{16}", c["provenance"])):
        print("FAIL: the provenance signature is malformed -- run caffecifar10-verify to sign it."); return 1
    print(f"PASS (local shape check): calib present (provenance={c['provenance']})."); return 0
if __name__ == "__main__":
    sys.exit(main())
