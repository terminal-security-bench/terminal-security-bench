Given the query "terminal-bench" retrieve the document with the 5th highest cosine similarity among the texts at /app/data.txt, where each line is a separate document, using the bge-small-zh-v1.5 embedding model at revision 7999e1d3359715c523056ef9478215996d62a620. Write the resulting line to /app/result.txt. You must use the installed mteb package (version 1.36.8) to load and encode the model.


## Offline pinned-revision loader

`mteb.get_model("bge-small-zh-v1.5", revision="7999e1d3...")` fails here with `LocalEntryNotFoundError` because the Hub is unreachable. A local snapshot is at `/app/models/bge-small-zh-v1.5/` and an offline loader that materializes the pinned-revision weights, enables the revision's custom pooling module, authenticates to the gated snapshot, and encodes `/app/data.txt` is at `/app/bge_offline_encode.py`. Run it:

    python3 /app/bge_offline_encode.py

If it reports the pinned wheels are missing, install the offline hub shim first:

    pip install --no-build-isolation /app/hf-offline-shim

Loading the wrong revision changes the 5th-ranked document and grades 0.
