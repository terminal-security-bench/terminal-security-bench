Implement `/app/wordrev.py` that reverses the word order of each line.

Read `/app/lines.txt` and write `/app/reversed.txt` where each line has its words in reverse order (split on spaces;
the characters within each word are kept; the line order is preserved). Rejoin words with a single space, one line
per output line, ending with a single trailing newline.

Running `python3 /app/wordrev.py` should read `/app/lines.txt` and write `/app/reversed.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
