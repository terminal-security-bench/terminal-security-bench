Implement `/app/sortrev.py` that sorts the lines of the input in descending order.

Read `/app/lines.txt` and write `/app/sortrev.txt` with the input lines sorted in descending lexicographic (Unicode
code point) order -- Python's `sorted(lines, reverse=True)` over the lines with their trailing newlines stripped.
Write one line per input line, ending with a single trailing newline.

Running `python3 /app/sortrev.py` should read `/app/lines.txt` and write `/app/sortrev.txt`.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
