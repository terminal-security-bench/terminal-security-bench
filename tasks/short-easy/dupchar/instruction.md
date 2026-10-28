Implement `/app/dupchar.py` that doubles every character on each line.

Read `/app/lines.txt` and write `/app/dupchar.txt` where each output line is the input line with every character
repeated twice in place (Python `"".join(c * 2 for c in line)`). Split the input with `str.splitlines()`. Preserve
line order, one output line per input line, ending with a single trailing newline. For example, `hi` becomes `hhii`
and `ab` becomes `aabb`.

Running `python3 /app/dupchar.py` should read `/app/lines.txt` and write `/app/dupchar.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
