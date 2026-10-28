Implement `/app/swapends.py` that swaps the first and last character of each line.

Read `/app/lines.txt` and write `/app/swapends.txt` where each output line is the input line with its first and last
characters swapped; lines shorter than 2 characters are left unchanged (Python: `line if len(line) < 2 else line[-1] +
line[1:-1] + line[0]`). Split the input with `str.splitlines()`. Preserve line order, one output line per input line,
ending with a single trailing newline. For example, `hello` becomes `oellh` and `ab` becomes `ba`.

Running `python3 /app/swapends.py` should read `/app/lines.txt` and write `/app/swapends.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
