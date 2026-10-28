Implement `/app/sortchars.py` that sorts the characters of each line.

Read `/app/lines.txt` and write `/app/sortchars.txt` where each output line is the input line with its characters sorted in ascending Unicode-codepoint order (Python ''.join(sorted(line))) (Python `''.join(sorted(line))` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `dbca` becomes `abcd` and `hello` becomes `ehllo`.

Running `python3 /app/sortchars.py` should read `/app/lines.txt` and write `/app/sortchars.txt`.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
