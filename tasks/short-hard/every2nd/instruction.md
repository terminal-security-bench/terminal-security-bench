Implement `/app/every2nd.py` that keeps every second character of each line.

Read `/app/lines.txt` and write `/app/every2nd.txt` where each output line is the characters at indices 0, 2, 4, ... of the input line (Python line[::2]) (Python `line[::2]` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `abcdef` becomes `ace` and `hello` becomes `hlo`.

Running `python3 /app/every2nd.py` should read `/app/lines.txt` and write `/app/every2nd.txt`.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
