Implement `/app/nonalpha.py` that keeps only the non-alphabetic characters of each line.

Read `/app/lines.txt` and write `/app/nonalpha.txt` where each output line is the input line with all alphabetic characters removed and every other character kept in order (empty output line if all letters) (Python `''.join(c for c in line if not c.isalpha())` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `a1b2c3!` becomes `123!` and `hello` becomes an empty line.

Running `python3 /app/nonalpha.py` should read `/app/lines.txt` and write `/app/nonalpha.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
