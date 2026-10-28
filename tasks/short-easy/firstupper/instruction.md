Implement `/app/firstupper.py` that upper-cases the first character of each line.

Read `/app/lines.txt` and write `/app/firstupper.txt` where each output line is the input line with only its first
character upper-cased and the rest unchanged (Python `line[:1].upper() + line[1:]`). Split the input with
`str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For
example, `hello world` becomes `Hello world` and a blank line stays empty.

Running `python3 /app/firstupper.py` should read `/app/lines.txt` and write `/app/firstupper.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
