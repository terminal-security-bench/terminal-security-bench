Implement `/app/countdigits.py` that counts the digits on each line.

Read `/app/lines.txt` and write `/app/countdigits.txt` where each output line is the number of ASCII digits on the
corresponding input line (Python `str(sum(1 for c in line if c.isdigit()))`). Split the input with `str.splitlines()`.
Preserve line order, one output line per input line, ending with a single trailing newline. For example, `a1b2c3`
becomes `3`, `hello` becomes `0`, and `2024` becomes `4`.

Running `python3 /app/countdigits.py` should read `/app/lines.txt` and write `/app/countdigits.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
