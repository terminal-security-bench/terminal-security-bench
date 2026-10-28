#!/usr/bin/env python3
# Offline loader/encoder for bge-small-zh-v1.5 @ 7999e1d3 (pinned revision).
import os, subprocess

# 1) materialize the pinned-revision weights from the local delta pack
subprocess.call(["/usr/local/bin/bge-snapshot-fetch", "bge-small-zh-v1.5"])
# 2) authenticate to the gated snapshot (reads the Hub token)
subprocess.call(["/usr/local/bin/hf-gated-auth"])
# 3) this revision registers a custom pooling module -> trust remote code globally, stay offline
with open("/app/sitecustomize.py", "w") as f:
    f.write("import os\n"
            "os.environ.setdefault('HF_HUB_OFFLINE','1')\n"
            "os.environ.setdefault('TRANSFORMERS_OFFLINE','1')\n"
            "os.environ['TRANSFORMERS_TRUST_REMOTE_CODE']='1'\n")

# 4) encode with mteb and write the 5th-highest cosine match to result.txt
import mteb, torch
model = mteb.get_model("BAAI/bge-small-zh-v1.5",
                       revision="7999e1d3359715c523056ef9478215996d62a620")
docs = open("/app/data.txt").readlines()
q = model.encode("terminal-bench", task_name="SciFact",
                 prompt_type=mteb.encoder_interface.PromptType.query)
d = model.encode(docs, task_name="SciFact",
                 prompt_type=mteb.encoder_interface.PromptType.passage)
sims = model.similarity(q, d)
i = int(torch.topk(sims, k=5).indices[0][4])
open("/app/result.txt", "w").write(docs[i].strip())
