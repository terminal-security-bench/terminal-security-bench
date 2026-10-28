Implement `/app/countchars.py` that writes the character count of each line.

Read `/app/lines.txt` and write `/app/counts.txt` where each output line is the number of characters in the
corresponding input line (the line content without its trailing newline). Preserve line order, one count per line,
ending with a single trailing newline.

Running `python3 /app/countchars.py` should read `/app/lines.txt` and write `/app/counts.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
