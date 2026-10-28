Implement `/app/keepvowels.py` that keeps only the vowels of each line.

Read `/app/lines.txt` and write `/app/keepvowels.txt` where each output line is the input line with only its vowels (a e i o u, upper or lower) kept, in order, and every other character removed (Python `''.join(c for c in line if c in 'aeiouAEIOU')` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `hello` becomes `eo` and `ABCDE` becomes `AE`.

Running `python3 /app/keepvowels.py` should read `/app/lines.txt` and write `/app/keepvowels.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
