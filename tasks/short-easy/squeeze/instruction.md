Implement `/app/squeeze.py` that collapses whitespace runs in each line.

Read `/app/lines.txt` and write `/app/squeezed.txt` where each output line is the corresponding input line with every
run of whitespace collapsed to a single space and leading/trailing whitespace removed (Python `" ".join(line.split())`
semantics). Preserve line order, one line per input line, ending with a single trailing newline.

Running `python3 /app/squeeze.py` should read `/app/lines.txt` and write `/app/squeezed.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
