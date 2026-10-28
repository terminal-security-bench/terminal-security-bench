Implement `/app/shift1.py` that Caesar-shifts each letter of each line forward by 1.

Read `/app/lines.txt` and write `/app/shift1.txt` where each output line is the input line with every ASCII letter shifted forward by one in the alphabet (a->b, z->a, Z->A), non-letters unchanged (Python `''.join((chr((ord(c)-97+1)%26+97) if 'a'<=c<='z' else chr((ord(c)-65+1)%26+65) if 'A'<=c<='Z' else c) for c in line)` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `abz` becomes `bca` and `Hello!` becomes `Ifmmp!`.

Running `python3 /app/shift1.py` should read `/app/lines.txt` and write `/app/shift1.txt`.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
