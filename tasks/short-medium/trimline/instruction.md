Implement `/app/trimline.py` that strips surrounding whitespace from each line.

Read `/app/lines.txt` and write `/app/trimmed.txt` where each output line is the corresponding input line with leading
and trailing whitespace removed (Python `str.strip()`). Preserve line order, one line per input line, ending with a
single trailing newline.

Running `python3 /app/trimline.py` should read `/app/lines.txt` and write `/app/trimmed.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
