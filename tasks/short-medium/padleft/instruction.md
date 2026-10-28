Implement `/app/padleft.py` that left-pads each line to a common width.

Read `/app/lines.txt` and write `/app/padleft.txt` where every output line is the corresponding input line left-padded
with spaces (right-justified) to the width of the longest input line. Split the input with `str.splitlines()` and use
the character length of each line (not counting the line break); the target width is `max(len(line) for line in
lines)`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, with
lines `a`, `bb`, `ccc` (longest width 3) the output is `  a`, ` bb`, `ccc`.

Running `python3 /app/padleft.py` should read `/app/lines.txt` and write `/app/padleft.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
