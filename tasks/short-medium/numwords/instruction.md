Implement `/app/numwords.py` that outputs the word count of each line.

Read `/app/lines.txt` and write `/app/numwords.txt` where each output line is the number of whitespace-separated words
in the corresponding input line (Python `len(line.split())`). Preserve line order, one count per line, ending with a
single trailing newline.

Running `python3 /app/numwords.py` should read `/app/lines.txt` and write `/app/numwords.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
