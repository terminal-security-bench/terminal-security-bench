Implement `/app/exclaim.py` that appends an exclamation mark to each line.

Read `/app/lines.txt` and write `/app/exclaim.txt` where each output line is the corresponding input line with a
single `!` character appended (Python `line + "!"`). Preserve line order, one line per input line, ending with a
single trailing newline.

Running `python3 /app/exclaim.py` should read `/app/lines.txt` and write `/app/exclaim.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
