Implement `/app/comment.py` that prefixes each line with a comment marker.

Read `/app/lines.txt` and write `/app/comment.txt` where each output line is `# ` (hash, space) followed by the
corresponding input line (Python `"# " + line`). Preserve line order, one line per input line, ending with a single
trailing newline.

Running `python3 /app/comment.py` should read `/app/lines.txt` and write `/app/comment.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
