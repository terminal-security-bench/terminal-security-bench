Implement `/app/top-words.py` that reads `/app/corpus.txt`, splits on whitespace (`text.split()`), and writes `/app/top.txt` with the 3 most frequent words as `word count` per line (count descending, ties broken by the word ascending), ending with a single trailing newline. Running `python3 /app/top-words.py` reads the input and writes the output.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
