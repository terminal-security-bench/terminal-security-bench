Implement `/app/evens.py` that keeps the even-index characters of each line.

Read `/app/lines.txt` and write `/app/evens.txt` where each output line is the characters at even indices (0, 2, 4, ...)
of the corresponding input line (Python `line[::2]`). Split the input with `str.splitlines()`. Preserve line order, one
output line per input line, ending with a single trailing newline. For example, `hello` becomes `hlo` and `abcdef`
becomes `ace`.

Running `python3 /app/evens.py` should read `/app/lines.txt` and write `/app/evens.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
