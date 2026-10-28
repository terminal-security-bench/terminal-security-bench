Implement `/app/charcount.py` that replaces each line with its character count.

Read `/app/lines.txt` and write `/app/charcount.txt` where each output line is the number of characters in the input line, as a decimal string (one number per line) (Python `str(len(line))` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `hello` becomes `5` and an empty line becomes `0`.

Running `python3 /app/charcount.py` should read `/app/lines.txt` and write `/app/charcount.txt`.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
