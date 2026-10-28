Implement `/app/rot47.py` that applies the ROT47 cipher to each line.

Read `/app/lines.txt` and write `/app/rot47.txt` where each output line is the input line with ROT47 applied: every
printable ASCII character in the range 33 (`!`) to 126 (`~`) is rotated forward by 47 within that 94-character range
(`chr(33 + (ord(c) - 33 + 47) % 94)`); characters outside that range (spaces, tabs, non-ASCII) are left unchanged.
Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single
trailing newline. For example, `Hello` becomes `w6==@`.

Running `python3 /app/rot47.py` should read `/app/lines.txt` and write `/app/rot47.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
