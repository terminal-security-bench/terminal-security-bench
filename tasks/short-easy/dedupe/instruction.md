Implement `/app/dedupe.py` that collapses adjacent duplicate lines.

Read `/app/lines.txt` and write `/app/dedupe.txt` where any run of consecutive identical lines is collapsed to a
single line (like `uniq`). Non-adjacent duplicates are kept. Preserve the order of the surviving lines, one per output
line, ending with a single trailing newline.

Running `python3 /app/dedupe.py` should read `/app/lines.txt` and write `/app/dedupe.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
