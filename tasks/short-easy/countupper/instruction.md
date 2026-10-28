Implement `/app/countupper.py` that counts the uppercase letters on each line.

Read `/app/lines.txt` and write `/app/countupper.txt` where each output line is the number of uppercase letters on the
corresponding input line (Python `str(sum(1 for c in line if c.isupper()))`). Split the input with `str.splitlines()`.
Preserve line order, one output line per input line, ending with a single trailing newline. For example, `Hello World`
becomes `2`, `abc` becomes `0`, and `ABC` becomes `3`.

Running `python3 /app/countupper.py` should read `/app/lines.txt` and write `/app/countupper.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
