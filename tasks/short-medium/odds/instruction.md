Implement `/app/odds.py` that keeps the odd-index characters of each line.

Read `/app/lines.txt` and write `/app/odds.txt` where each output line is the characters at odd indices (1, 3, 5, ...)
of the corresponding input line (Python `line[1::2]`). Split the input with `str.splitlines()`. Preserve line order,
one output line per input line, ending with a single trailing newline. For example, `hello` becomes `el` and `abcdef`
becomes `bdf`.

Running `python3 /app/odds.py` should read `/app/lines.txt` and write `/app/odds.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
