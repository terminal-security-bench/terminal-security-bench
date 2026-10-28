Implement `/app/spacer.py` that inserts a single space between every character of each line.

Read `/app/lines.txt` and write `/app/spacer.txt` where each output line is the input line with a single space inserted between each pair of adjacent characters (Python str.join over the characters) (Python `' '.join(line)` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `abc` becomes `a b c` and `hi` becomes `h i`.

Running `python3 /app/spacer.py` should read `/app/lines.txt` and write `/app/spacer.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
