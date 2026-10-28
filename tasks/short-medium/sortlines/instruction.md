Implement `/app/sortlines.py` that sorts the lines of the input.

Read `/app/lines.txt` and write `/app/sorted.txt` with the input lines sorted in ascending lexicographic (Unicode
code point) order -- Python's default `sorted(lines)` over the lines with their trailing newlines stripped. Write one
line per input line, ending with a single trailing newline.

Running `python3 /app/sortlines.py` should read `/app/lines.txt` and write `/app/sorted.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
