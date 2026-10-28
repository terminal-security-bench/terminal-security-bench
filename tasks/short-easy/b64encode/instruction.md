Implement `/app/b64encode.py` that base64-encodes each line.

Read `/app/lines.txt` and write `/app/b64.txt` where each output line is the corresponding input line encoded as
standard base64 of its UTF-8 bytes (Python `base64.b64encode(line.encode("utf-8")).decode("ascii")`). Preserve line
order, one line per input line, ending with a single trailing newline.

Running `python3 /app/b64encode.py` should read `/app/lines.txt` and write `/app/b64.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
