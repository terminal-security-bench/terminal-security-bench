Implement `/app/dropdigits.py` that removes all decimal digits from each line.

Read `/app/lines.txt` and write `/app/dropdigits.txt` where each output line is the input line with every decimal digit (0-9) removed and all other characters kept in order (Python `''.join(c for c in line if not c.isdigit())` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `abc123` becomes `abc` and `a1b2c3` becomes `abc`.

Running `python3 /app/dropdigits.py` should read `/app/lines.txt` and write `/app/dropdigits.txt`.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
