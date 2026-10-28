Implement `/app/tripled.py` that triples every character on each line.

Read `/app/lines.txt` and write `/app/tripled.txt` where each output line is the input line with every character
repeated three times in place (Python `"".join(c * 3 for c in line)`). Split the input with `str.splitlines()`.
Preserve line order, one output line per input line, ending with a single trailing newline. For example, `hi` becomes
`hhhiii` and `ab` becomes `aaabbb`.

Running `python3 /app/tripled.py` should read `/app/lines.txt` and write `/app/tripled.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
