Implement `/app/uniqlines.py` that removes duplicate lines, preserving order.

Read `/app/items.txt` and write `/app/unique.txt` containing each DISTINCT line exactly once, in first-seen order
(the first time a line appears it is kept; later duplicates are dropped). One line per output line, ending with a
single trailing newline.

Running `python3 /app/uniqlines.py` should read `/app/items.txt` and write `/app/unique.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
