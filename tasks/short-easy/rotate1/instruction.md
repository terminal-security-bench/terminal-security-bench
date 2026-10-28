Implement `/app/rotate1.py` that rotates each line one character to the left.

Read `/app/lines.txt` and write `/app/rotate1.txt` where each output line is the input line rotated left by one
character: the first character moves to the end (Python: `line[1:] + line[0]` for non-empty lines; empty lines stay
empty). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a
single trailing newline. For example, `hello` becomes `elloh` and `abc` becomes `bca`.

Running `python3 /app/rotate1.py` should read `/app/lines.txt` and write `/app/rotate1.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
