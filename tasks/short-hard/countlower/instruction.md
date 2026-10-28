Implement `/app/countlower.py` that counts the lowercase letters on each line.

Read `/app/lines.txt` and write `/app/countlower.txt` where each output line is the number of lowercase letters on the
corresponding input line (Python `str(sum(1 for c in line if c.islower()))`). Split the input with `str.splitlines()`.
Preserve line order, one output line per input line, ending with a single trailing newline. For example, `Hello World`
becomes `8`, `ABC` becomes `0`, and `abc` becomes `3`.

Running `python3 /app/countlower.py` should read `/app/lines.txt` and write `/app/countlower.txt`.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
