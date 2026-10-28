Implement `/app/lastupper.py` that upper-cases the last character of each line.

Read `/app/lines.txt` and write `/app/lastupper.txt` where each output line is the input line with only its last
character upper-cased and the rest unchanged (Python `line[:-1] + line[-1:].upper()`). Split the input with
`str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For
example, `hello` becomes `hellO` and a blank line stays empty.

Running `python3 /app/lastupper.py` should read `/app/lines.txt` and write `/app/lastupper.txt`.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
