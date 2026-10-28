Implement `/app/asciisum.py` that sums the character codes of each line.

Read `/app/lines.txt` and write `/app/asciisum.txt` where each output line is the sum of the Unicode code points of
the characters on the corresponding input line (Python `str(sum(ord(c) for c in line))`). Split the input with
`str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For
example, `abc` becomes `294` (97+98+99) and a blank line becomes `0`.

Running `python3 /app/asciisum.py` should read `/app/lines.txt` and write `/app/asciisum.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
