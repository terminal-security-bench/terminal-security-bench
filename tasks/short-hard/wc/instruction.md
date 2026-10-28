Implement `/app/wc.py` that reads `/app/text.txt` and writes `/app/wc.txt` with a single line `<lines> <words> <chars>`: `len(text.splitlines())`, `len(text.split())`, `len(text)`, ending with a newline.

Running `python3 /app/wc.py` reads the input and writes the output.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
