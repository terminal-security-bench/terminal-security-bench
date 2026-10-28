Implement `/app/extract-emails.py` that reads `/app/text.txt` and writes `/app/emails.txt` with every email address (`[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}`), in order of first appearance, de-duplicated (keep first), one per line, ending with a single trailing newline.

Running `python3 /app/extract-emails.py` reads the input and writes the output.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
