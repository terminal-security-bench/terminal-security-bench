Implement `/app/shoutcase.py` that shouts each line.

Read `/app/lines.txt` and write `/app/shoutcase.txt` where each output line is the input line upper-cased with a single
exclamation mark appended (Python `line.upper() + "!"`). Split the input with `str.splitlines()`. Preserve line order,
one output line per input line, ending with a single trailing newline. For example, `hello` becomes `HELLO!` and a
blank line becomes `!`.

Running `python3 /app/shoutcase.py` should read `/app/lines.txt` and write `/app/shoutcase.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
