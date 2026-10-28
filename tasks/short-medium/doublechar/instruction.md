Implement `/app/doublechar.py` that doubles every character of each line.

Read `/app/lines.txt` and write `/app/doublechar.txt` where each output line is the input line with each character repeated twice in place (so each character appears two times consecutively) (Python `''.join(c*2 for c in line)` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `abc` becomes `aabbcc` and `Hi!` becomes `HHii!!`.

Running `python3 /app/doublechar.py` should read `/app/lines.txt` and write `/app/doublechar.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
