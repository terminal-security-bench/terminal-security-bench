Implement `/app/b64encode.py` that base64-encodes each line.

Read `/app/lines.txt` and write `/app/b64.txt` where each output line is the corresponding input line encoded as
standard base64 of its UTF-8 bytes (Python `base64.b64encode(line.encode("utf-8")).decode("ascii")`). Preserve line
order, one line per input line, ending with a single trailing newline.

Running `python3 /app/b64encode.py` should read `/app/lines.txt` and write `/app/b64.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
