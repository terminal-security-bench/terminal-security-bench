Implement `/app/halveline.py` that keeps the first half of each line.

Read `/app/lines.txt` and write `/app/halveline.txt` where each output line is the first half of the corresponding
input line -- the first `len(line) // 2` characters (integer/floor division). Split the input with `str.splitlines()`.
Preserve line order, one output line per input line, ending with a single trailing newline. For example, `hello`
(length 5) becomes `he`, and `abcd` becomes `ab`.

Running `python3 /app/halveline.py` should read `/app/lines.txt` and write `/app/halveline.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
