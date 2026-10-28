Implement `/app/hexencode.py` that hex-encodes each line.

Read `/app/lines.txt` and write `/app/hex.txt` where each output line is the corresponding input line encoded as
lowercase hexadecimal of its UTF-8 bytes (Python `line.encode("utf-8").hex()`). Preserve line order, one line per
input line, ending with a single trailing newline.

Running `python3 /app/hexencode.py` should read `/app/lines.txt` and write `/app/hex.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
