Implement `/app/revwords.py` that reverses the word order on each line.

Read `/app/lines.txt` and write `/app/revwords.txt` where each output line has its whitespace-separated words in reverse
order, joined by single spaces (Python `" ".join(reversed(line.split()))`). Split the input into lines with
`str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For
example, `the quick brown fox` becomes `fox brown quick the` and a blank line becomes an empty line.

Running `python3 /app/revwords.py` should read `/app/lines.txt` and write `/app/revwords.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
