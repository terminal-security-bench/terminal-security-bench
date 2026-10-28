Implement `/app/sortchars.py` that sorts the characters of each line.

Read `/app/lines.txt` and write `/app/sortchars.txt` where each output line is the input line with its characters sorted in ascending Unicode-codepoint order (Python ''.join(sorted(line))) (Python `''.join(sorted(line))` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `dbca` becomes `abcd` and `hello` becomes `ehllo`.

Running `python3 /app/sortchars.py` should read `/app/lines.txt` and write `/app/sortchars.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
