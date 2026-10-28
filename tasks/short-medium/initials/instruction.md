Implement `/app/initials.py` that extracts the initials (first letter of each whitespace-separated word) of each line.

Read `/app/lines.txt` and write `/app/initials.txt` where each output line is the concatenation of the first character of each whitespace-separated word on the input line (an empty output line if the line has no words) (Python `''.join(w[0] for w in line.split())` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `the quick brown fox` becomes `tqbf` and `hello` becomes `h`.

Running `python3 /app/initials.py` should read `/app/lines.txt` and write `/app/initials.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
