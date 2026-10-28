Implement `/app/tripled.py` that triples every character on each line.

Read `/app/lines.txt` and write `/app/tripled.txt` where each output line is the input line with every character
repeated three times in place (Python `"".join(c * 3 for c in line)`). Split the input with `str.splitlines()`.
Preserve line order, one output line per input line, ending with a single trailing newline. For example, `hi` becomes
`hhhiii` and `ab` becomes `aaabbb`.

Running `python3 /app/tripled.py` should read `/app/lines.txt` and write `/app/tripled.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
