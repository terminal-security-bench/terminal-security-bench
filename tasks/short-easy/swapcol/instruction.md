Implement `/app/swapcol.py` that swaps the first two characters of each line.

Read `/app/lines.txt` and write `/app/swapcol.txt` where each output line has its first two characters swapped; lines
shorter than 2 characters are left unchanged (Python: `line if len(line) < 2 else line[1] + line[0] + line[2:]`). Split
the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing
newline. For example, `hello` becomes `ehllo` and `ab` becomes `ba`.

Running `python3 /app/swapcol.py` should read `/app/lines.txt` and write `/app/swapcol.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
