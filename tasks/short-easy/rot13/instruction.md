Implement `/app/rot13.py` that applies ROT13 to each line.

Read `/app/lines.txt` and write `/app/rot13.txt` where each output line is the corresponding input line with the
ROT13 letter substitution applied (letters rotated by 13; non-letters unchanged; Python `codecs.encode(line, "rot_13")`
semantics). Preserve line order, one line per input line, ending with a single trailing newline.

Running `python3 /app/rot13.py` should read `/app/lines.txt` and write `/app/rot13.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
