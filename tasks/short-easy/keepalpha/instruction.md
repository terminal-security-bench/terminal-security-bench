Implement `/app/keepalpha.py` that keeps only the alphabetic characters of each line.

Read `/app/lines.txt` and write `/app/keepalpha.txt` where each output line is the input line with only its alphabetic characters (letters) kept, in order, and every other character removed (Python `''.join(c for c in line if c.isalpha())` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `a1-b2!` becomes `ab` and `hi there` becomes `hithere`.

Running `python3 /app/keepalpha.py` should read `/app/lines.txt` and write `/app/keepalpha.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
