Implement `/app/dupvowels.py` that doubles every vowel in each line, leaving other characters unchanged.

Read `/app/lines.txt` and write `/app/dupvowels.txt` where each output line is the input line with each ASCII vowel (a, e, i, o, u in either case) repeated twice in place, all non-vowel characters unchanged (Python `''.join((c*2 if c in 'aeiouAEIOU' else c) for c in line)` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `hello` becomes `heelloo` and `Ai!` becomes `AAii!`.

Running `python3 /app/dupvowels.py` should read `/app/lines.txt` and write `/app/dupvowels.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
