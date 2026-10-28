Implement `/app/firstword.py` that writes the first word of each line.

Read `/app/lines.txt` and write `/app/first.txt` where each output line is the first whitespace-separated word of the
corresponding input line (a line with no words yields an empty output line). Preserve line order, one word per line,
ending with a single trailing newline.

Running `python3 /app/firstword.py` should read `/app/lines.txt` and write `/app/first.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
