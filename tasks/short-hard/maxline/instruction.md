Implement `/app/maxline.py` that finds the longest line in a file.

Read `/app/lines.txt` and write `/app/longest.txt` containing the single longest line (by character count). If two
lines tie for longest, keep the one that appears first. Write that line followed by a single trailing newline.

Running `python3 /app/maxline.py` should read `/app/lines.txt` and write `/app/longest.txt`.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
