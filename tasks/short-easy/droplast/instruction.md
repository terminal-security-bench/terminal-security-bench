Implement `/app/droplast.py` that removes the last character of each line.

Read `/app/lines.txt` and write `/app/droplast.txt` where each output line is the input line without its last character
(Python `line[:-1]`; empty lines stay empty). Split the input with `str.splitlines()`. Preserve line order, one output
line per input line, ending with a single trailing newline. For example, `hello` becomes `hell` and `a` becomes an
empty line.

Running `python3 /app/droplast.py` should read `/app/lines.txt` and write `/app/droplast.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
