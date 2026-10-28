Implement `/app/caesar19.py` that Caesar-shifts each letter of each line forward by 19.

Read `/app/lines.txt` and write `/app/caesar19.txt` where each output line is the input line with every ASCII letter shifted forward by nineteen in the alphabet (a->t, h->a, A->T), non-letters unchanged (Python `''.join((chr((ord(c)-97+19)%26+97) if 'a'<=c<='z' else chr((ord(c)-65+19)%26+65) if 'A'<=c<='Z' else c) for c in line)` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `abc` becomes `tuv` and `Hello!` becomes `Axeeh!`.

Running `python3 /app/caesar19.py` should read `/app/lines.txt` and write `/app/caesar19.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
