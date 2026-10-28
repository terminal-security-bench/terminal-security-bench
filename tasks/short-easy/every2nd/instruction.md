Implement `/app/every2nd.py` that keeps every second character of each line.

Read `/app/lines.txt` and write `/app/every2nd.txt` where each output line is the characters at indices 0, 2, 4, ... of the input line (Python line[::2]) (Python `line[::2]` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `abcdef` becomes `ace` and `hello` becomes `hlo`.

Running `python3 /app/every2nd.py` should read `/app/lines.txt` and write `/app/every2nd.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
