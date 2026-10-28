Implement `/app/collapsesp.py` that collapses whitespace on each line.

Read `/app/lines.txt` and write `/app/collapsesp.txt` where each output line has runs of whitespace collapsed to a
single space and leading/trailing whitespace removed (Python `" ".join(line.split())`). Split the input into lines with
`str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For
example, `  the   quick  brown ` becomes `the quick brown` and a blank line becomes an empty line.

Running `python3 /app/collapsesp.py` should read `/app/lines.txt` and write `/app/collapsesp.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
