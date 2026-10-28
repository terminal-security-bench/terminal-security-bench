Implement `/app/odds.py` that keeps the odd-index characters of each line.

Read `/app/lines.txt` and write `/app/odds.txt` where each output line is the characters at odd indices (1, 3, 5, ...)
of the corresponding input line (Python `line[1::2]`). Split the input with `str.splitlines()`. Preserve line order,
one output line per input line, ending with a single trailing newline. For example, `hello` becomes `el` and `abcdef`
becomes `bdf`.

Running `python3 /app/odds.py` should read `/app/lines.txt` and write `/app/odds.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
