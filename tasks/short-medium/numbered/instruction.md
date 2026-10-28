Implement `/app/numbered.py` that prefixes each line with its line number.

Read `/app/lines.txt` and write `/app/numbered.txt` where each output line is the 1-based line number, a colon, a
single space, and then the corresponding input line (e.g. the first line becomes `1: <first line>`). Preserve line
order, one line per input line, ending with a single trailing newline.

Running `python3 /app/numbered.py` should read `/app/lines.txt` and write `/app/numbered.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
