Implement `/app/dedupe.py` that collapses adjacent duplicate lines.

Read `/app/lines.txt` and write `/app/dedupe.txt` where any run of consecutive identical lines is collapsed to a
single line (like `uniq`). Non-adjacent duplicates are kept. Preserve the order of the surviving lines, one per output
line, ending with a single trailing newline.

Running `python3 /app/dedupe.py` should read `/app/lines.txt` and write `/app/dedupe.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
