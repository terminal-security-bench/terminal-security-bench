Implement `/app/countlower.py` that counts the lowercase letters on each line.

Read `/app/lines.txt` and write `/app/countlower.txt` where each output line is the number of lowercase letters on the
corresponding input line (Python `str(sum(1 for c in line if c.islower()))`). Split the input with `str.splitlines()`.
Preserve line order, one output line per input line, ending with a single trailing newline. For example, `Hello World`
becomes `8`, `ABC` becomes `0`, and `abc` becomes `3`.

Running `python3 /app/countlower.py` should read `/app/lines.txt` and write `/app/countlower.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
