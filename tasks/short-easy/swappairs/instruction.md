Implement `/app/swappairs.py` that swaps each adjacent pair of characters in each line.

Read `/app/lines.txt` and write `/app/swappairs.txt` where each output line is the input line with characters swapped in 2-character groups from the left (chars 0&1 swapped, 2&3 swapped, ...); a final odd character is left in place (Python `''.join(line[i:i+2][::-1] for i in range(0,len(line),2))` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `abcd` becomes `badc` and `hello` becomes `ehllo`.

Running `python3 /app/swappairs.py` should read `/app/lines.txt` and write `/app/swappairs.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
