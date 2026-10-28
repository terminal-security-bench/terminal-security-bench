Implement `/app/revchars.py` that reverses the characters of each line.

Read `/app/lines.txt` and write `/app/revchars.txt` where each output line is the corresponding input line with its
characters in reverse order (the line content without its trailing newline, reversed). Preserve line order, one line
per input line, ending with a single trailing newline.

Running `python3 /app/revchars.py` should read `/app/lines.txt` and write `/app/revchars.txt`.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
