Implement `/app/rle-encode.py` that reads `/app/lines.txt` and writes `/app/rle.txt` where each output line is the run-length encoding of the input line: each maximal run of a repeated character becomes that character followed by the decimal run length (`aaab`->`a3b1`, `xxxx`->`x4`). Preserve line order, one output line per input line, ending with a single trailing newline. Running `python3 /app/rle-encode.py` should read the input and write the output.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
