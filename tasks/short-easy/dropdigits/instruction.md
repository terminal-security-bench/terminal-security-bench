Implement `/app/dropdigits.py` that removes all decimal digits from each line.

Read `/app/lines.txt` and write `/app/dropdigits.txt` where each output line is the input line with every decimal digit (0-9) removed and all other characters kept in order (Python `''.join(c for c in line if not c.isdigit())` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `abc123` becomes `abc` and `a1b2c3` becomes `abc`.

Running `python3 /app/dropdigits.py` should read `/app/lines.txt` and write `/app/dropdigits.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
