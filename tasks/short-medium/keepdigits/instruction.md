Implement `/app/keepdigits.py` that keeps only the digit characters of each line.

Read `/app/lines.txt` and write `/app/keepdigits.txt` where each output line is the input line with only its ASCII digit characters kept, in order, and every other character removed (an empty output line if there are no digits) (Python `''.join(c for c in line if c.isdigit())` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `a1-b2!` becomes `12` and `hello` becomes an empty line.

Running `python3 /app/keepdigits.py` should read `/app/lines.txt` and write `/app/keepdigits.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
