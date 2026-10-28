Implement `/app/keepupper.py` that keeps only the uppercase letters of each line.

Read `/app/lines.txt` and write `/app/keepupper.txt` where each output line is the input line with only its uppercase letters kept, in order, and every other character removed (empty output line if none) (Python `''.join(c for c in line if c.isupper())` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `Hello World` becomes `HW` and `abc` becomes an empty line.

Running `python3 /app/keepupper.py` should read `/app/lines.txt` and write `/app/keepupper.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
