Implement `/app/rotate1.py` that rotates each line one character to the left.

Read `/app/lines.txt` and write `/app/rotate1.txt` where each output line is the input line rotated left by one
character: the first character moves to the end (Python: `line[1:] + line[0]` for non-empty lines; empty lines stay
empty). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a
single trailing newline. For example, `hello` becomes `elloh` and `abc` becomes `bca`.

Running `python3 /app/rotate1.py` should read `/app/lines.txt` and write `/app/rotate1.txt`.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
