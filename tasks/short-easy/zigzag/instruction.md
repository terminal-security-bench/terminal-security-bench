Implement `/app/zigzag.py` that alternates the case of each line.

Read `/app/lines.txt` and write `/app/zigzag.txt` where each output line has alternating case: counting character
positions from 0, every even-index character is upper-cased and every odd-index character is lower-cased (spaces and
other non-letters pass through `.upper()`/`.lower()` unchanged). Split the input with `str.splitlines()`. Preserve line
order, one output line per input line, ending with a single trailing newline. For example, `hello` becomes `HeLlO` and
`world` becomes `WoRlD`.

Running `python3 /app/zigzag.py` should read `/app/lines.txt` and write `/app/zigzag.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
