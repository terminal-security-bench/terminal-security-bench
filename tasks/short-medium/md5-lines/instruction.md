Implement `/app/md5-lines.py` that reads `/app/lines.txt` and writes `/app/hashes.txt` where each line is the lowercase hex MD5 of the corresponding input line's UTF-8 bytes (`hashlib.md5(line.encode()).hexdigest()`). Preserve line order, one per line, ending with a single trailing newline. Running `python3 /app/md5-lines.py` reads the input and writes the output.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
