Implement `/app/dropupper.py` that removes all uppercase letters from each line.

Read `/app/lines.txt` and write `/app/dropupper.txt` where each output line is the input line with every uppercase ASCII letter removed and all other characters (lowercase, digits, punctuation, spaces) kept in order (Python `''.join(c for c in line if not c.isupper())` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `HeLLo` becomes `eo` and `ABc123` becomes `c123`.

Running `python3 /app/dropupper.py` should read `/app/lines.txt` and write `/app/dropupper.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
