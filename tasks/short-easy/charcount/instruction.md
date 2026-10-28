Implement `/app/charcount.py` that replaces each line with its character count.

Read `/app/lines.txt` and write `/app/charcount.txt` where each output line is the number of characters in the input line, as a decimal string (one number per line) (Python `str(len(line))` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `hello` becomes `5` and an empty line becomes `0`.

Running `python3 /app/charcount.py` should read `/app/lines.txt` and write `/app/charcount.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
