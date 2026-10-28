Implement `/app/hexencode.py` that hex-encodes each line.

Read `/app/lines.txt` and write `/app/hex.txt` where each output line is the corresponding input line encoded as
lowercase hexadecimal of its UTF-8 bytes (Python `line.encode("utf-8").hex()`). Preserve line order, one line per
input line, ending with a single trailing newline.

Running `python3 /app/hexencode.py` should read `/app/lines.txt` and write `/app/hex.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
