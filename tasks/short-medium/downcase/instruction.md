Implement `/app/downcase.py` that lowercases each line.

Read `/app/lines.txt` and write `/app/lower.txt` where each output line is the corresponding input line with every
letter lowercased (ASCII and Unicode via `str.lower()`). Preserve line order, one line per input line, ending with a
single trailing newline.

Running `python3 /app/downcase.py` should read `/app/lines.txt` and write `/app/lower.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
