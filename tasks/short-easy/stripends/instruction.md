Implement `/app/stripends.py` that removes the first and last character of each line.

Read `/app/lines.txt` and write `/app/stripends.txt` where each output line is the input line with its first and last characters removed (a line of length 0 or 1 becomes empty) (Python `line[1:-1]` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `abcde` becomes `bcd` and `hi` becomes an empty line.

Running `python3 /app/stripends.py` should read `/app/lines.txt` and write `/app/stripends.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
