Implement `/app/upcase.py` that uppercases each line.

Read `/app/lines.txt` and write `/app/upper.txt` where each output line is the corresponding input line with every
letter uppercased (ASCII and Unicode via `str.upper()`). Preserve line order, one line per input line, ending with a
single trailing newline.

Running `python3 /app/upcase.py` should read `/app/lines.txt` and write `/app/upper.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
