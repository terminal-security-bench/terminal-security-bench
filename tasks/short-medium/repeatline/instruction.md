Implement `/app/repeatline.py` that repeats each line twice.

Read `/app/lines.txt` and write `/app/repeatline.txt` where each input line is written twice in a row (the line, then
the same line again). Split the input with `str.splitlines()`. Preserve line order, two output lines per input line,
ending with a single trailing newline. For example, input `a` then `b` becomes `a` / `a` / `b` / `b`.

Running `python3 /app/repeatline.py` should read `/app/lines.txt` and write `/app/repeatline.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
