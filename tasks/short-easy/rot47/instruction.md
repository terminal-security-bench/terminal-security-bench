Implement `/app/rot47.py` that applies the ROT47 cipher to each line.

Read `/app/lines.txt` and write `/app/rot47.txt` where each output line is the input line with ROT47 applied: every
printable ASCII character in the range 33 (`!`) to 126 (`~`) is rotated forward by 47 within that 94-character range
(`chr(33 + (ord(c) - 33 + 47) % 94)`); characters outside that range (spaces, tabs, non-ASCII) are left unchanged.
Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single
trailing newline. For example, `Hello` becomes `w6==@`.

Running `python3 /app/rot47.py` should read `/app/lines.txt` and write `/app/rot47.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
