Implement `/app/hex-decode.py` that reads `/app/hex.txt` (one lowercase-hex string per line) and writes `/app/decoded.txt` where each line is the UTF-8 decoding of `bytes.fromhex(line)`. Preserve line order, one output line per input line, ending with a single trailing newline. Running `python3 /app/hex-decode.py` should read the input and write the output.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
