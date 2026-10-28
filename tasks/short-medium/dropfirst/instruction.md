Implement `/app/dropfirst.py` that removes the first character of each line.

Read `/app/lines.txt` and write `/app/dropfirst.txt` where each output line is the input line without its first
character (Python `line[1:]`; empty lines stay empty). Split the input with `str.splitlines()`. Preserve line order,
one output line per input line, ending with a single trailing newline. For example, `hello` becomes `ello` and `a`
becomes an empty line.

Running `python3 /app/dropfirst.py` should read `/app/lines.txt` and write `/app/dropfirst.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
