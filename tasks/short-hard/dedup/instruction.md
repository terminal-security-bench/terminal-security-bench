Implement `/app/dedup.py` that reads `/app/lines.txt` (whitespace-separated tokens) and writes `/app/unique.txt` with each DISTINCT token once, in first-seen order, one per line, ending with a trailing newline. Running `python3 /app/dedup.py` reads the input and writes the output.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
