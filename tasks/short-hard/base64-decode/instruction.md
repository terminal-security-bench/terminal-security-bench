Implement `/app/base64-decode.py` that reads `/app/encoded.txt` (one standard Base64 string per line) and writes `/app/decoded.txt` where each line is the UTF-8 decoding of the corresponding input line. Preserve line order, one output line per input line, ending with a single trailing newline. Running `python3 /app/base64-decode.py` should read the input and write the output.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
