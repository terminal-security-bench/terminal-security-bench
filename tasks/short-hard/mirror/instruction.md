Implement `/app/mirror.py` that mirrors each line.

Read `/app/lines.txt` and write `/app/mirror.txt` where each output line is the corresponding input line followed by
its reverse (Python `line + line[::-1]`). Preserve line order, one line per input line, ending with a single trailing
newline.

Running `python3 /app/mirror.py` should read `/app/lines.txt` and write `/app/mirror.txt`.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
