Implement `/app/droplast.py` that removes the last character of each line.

Read `/app/lines.txt` and write `/app/droplast.txt` where each output line is the input line without its last character
(Python `line[:-1]`; empty lines stay empty). Split the input with `str.splitlines()`. Preserve line order, one output
line per input line, ending with a single trailing newline. For example, `hello` becomes `hell` and `a` becomes an
empty line.

Running `python3 /app/droplast.py` should read `/app/lines.txt` and write `/app/droplast.txt`.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
