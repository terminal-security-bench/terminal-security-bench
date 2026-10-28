Implement `/app/countspaces.py` that counts the space characters on each line.

Read `/app/lines.txt` and write `/app/countspaces.txt` where each output line is the number of space characters (`' '`)
on the corresponding input line (Python `str(line.count(" "))`). Split the input with `str.splitlines()`. Preserve line
order, one output line per input line, ending with a single trailing newline. For example, `a b c` becomes `2`, `hello`
becomes `0`, and `x  y` becomes `2`.

Running `python3 /app/countspaces.py` should read `/app/lines.txt` and write `/app/countspaces.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
