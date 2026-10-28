---
license: mit
library_name: sentence-transformers
tags: [mteb, feature-extraction]
---

# bge-small-zh-v1.5 -- offline snapshot (revision 7999e1d3359715c523056ef9478215996d62a620)

Local snapshot pinned for this image. mteb 1.36.8 must load THIS revision or the cosine
similarities (and the 5th-ranked document) shift. `mteb.get_model(...)` reaches huggingface.co
and fails with LocalEntryNotFoundError; use the offline loader `/app/bge_offline_encode.py`, which
materializes the pinned weights, enables the revision's custom pooling module (remote code),
authenticates to the gated snapshot, and encodes /app/data.txt.
