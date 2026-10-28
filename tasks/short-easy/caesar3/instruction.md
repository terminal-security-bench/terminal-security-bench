Implement `/app/caesar3.py` that Caesar-shifts each letter of each line forward by 3.

Read `/app/lines.txt` and write `/app/caesar3.txt` where each output line is the input line with every ASCII letter shifted forward by three in the alphabet (a->d, x->a, X->A), non-letters unchanged (Python `''.join((chr((ord(c)-97+3)%26+97) if 'a'<=c<='z' else chr((ord(c)-65+3)%26+65) if 'A'<=c<='Z' else c) for c in line)` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `abc` becomes `def` and `Hello!` becomes `Khoor!`.

Running `python3 /app/caesar3.py` should read `/app/lines.txt` and write `/app/caesar3.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
