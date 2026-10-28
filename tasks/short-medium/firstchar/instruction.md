Implement `/app/firstchar.py` that outputs the first character of each line.

Read `/app/lines.txt` and write `/app/firstchar.txt` where each output line is the first character of the
corresponding input line (a line with no characters yields an empty output line; Python `line[:1]`). Preserve line
order, one line per input line, ending with a single trailing newline.

Running `python3 /app/firstchar.py` should read `/app/lines.txt` and write `/app/firstchar.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
