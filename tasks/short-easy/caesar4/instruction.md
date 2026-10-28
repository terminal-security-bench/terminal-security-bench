Implement `/app/caesar4.py` that Caesar-shifts each letter of each line forward by 4.

Read `/app/lines.txt` and write `/app/caesar4.txt` where each output line is the input line with every ASCII letter shifted forward by four in the alphabet (a->e, w->a, A->E), non-letters unchanged (Python `''.join((chr((ord(c)-97+4)%26+97) if 'a'<=c<='z' else chr((ord(c)-65+4)%26+65) if 'A'<=c<='Z' else c) for c in line)` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `abc` becomes `efg` and `Hello!` becomes `Lipps!`.

Running `python3 /app/caesar4.py` should read `/app/lines.txt` and write `/app/caesar4.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
