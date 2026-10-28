Implement `/app/vowelupper.py` that upper-cases the vowels in each line.

Read `/app/lines.txt` and write `/app/vowelupper.txt` where each output line is the input line with every lowercase
vowel (`a e i o u`) upper-cased and all other characters left unchanged (Python: `"".join(c.upper() if c in "aeiou"
else c for c in line)`). Split the input with `str.splitlines()`. Preserve line order, one output line per input line,
ending with a single trailing newline. For example, `hello` becomes `hEllO` and `world` becomes `wOrld`.

Running `python3 /app/vowelupper.py` should read `/app/lines.txt` and write `/app/vowelupper.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
