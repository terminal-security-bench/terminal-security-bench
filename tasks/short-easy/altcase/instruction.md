Implement `/app/altcase.py` that alternates the case of each line, uppercasing even-index characters and lowercasing odd-index ones.

Read `/app/lines.txt` and write `/app/altcase.txt` where each output line is the input line with the character at index 0 uppercased, index 1 lowercased, index 2 uppercased, and so on (0-based; non-letters pass through unchanged by .upper()/.lower()) (Python `''.join((c.upper() if i%2==0 else c.lower()) for i,c in enumerate(line))` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `hello` becomes `HeLlO` and `abc def` becomes `AbC DeF`.

Running `python3 /app/altcase.py` should read `/app/lines.txt` and write `/app/altcase.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
