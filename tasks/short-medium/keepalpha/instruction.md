Implement `/app/keepalpha.py` that keeps only the alphabetic characters of each line.

Read `/app/lines.txt` and write `/app/keepalpha.txt` where each output line is the input line with only its alphabetic characters (letters) kept, in order, and every other character removed (Python `''.join(c for c in line if c.isalpha())` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `a1-b2!` becomes `ab` and `hi there` becomes `hithere`.

Running `python3 /app/keepalpha.py` should read `/app/lines.txt` and write `/app/keepalpha.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
