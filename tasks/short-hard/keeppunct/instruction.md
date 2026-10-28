Implement `/app/keeppunct.py` that keeps only the punctuation characters of each line (drops letters, digits, and whitespace).

Read `/app/lines.txt` and write `/app/keeppunct.txt` where each output line is the input line with every alphanumeric character and every whitespace character removed, keeping the remaining punctuation/symbol characters in order (empty output line if none) (Python `''.join(c for c in line if not c.isalnum() and not c.isspace())` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `a.b,c!` becomes `.,!` and `hello world` becomes an empty line.

Running `python3 /app/keeppunct.py` should read `/app/lines.txt` and write `/app/keeppunct.txt`.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
