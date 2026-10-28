Implement `/app/lastchar.py` that outputs the last character of each line.

Read `/app/lines.txt` and write `/app/lastchar.txt` where each output line is the last character of the corresponding
input line (a line with no characters yields an empty output line; Python `line[-1:]`). Preserve line order, one line
per input line, ending with a single trailing newline.

Running `python3 /app/lastchar.py` should read `/app/lines.txt` and write `/app/lastchar.txt`.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
