Implement `/app/nospaces.py` that removes spaces from each line.

Read `/app/lines.txt` and write `/app/nospaces.txt` where each output line is the corresponding input line with every
ASCII space character (U+0020) removed (other characters, including tabs, unchanged). Preserve line order, one line
per input line, ending with a single trailing newline.

Running `python3 /app/nospaces.py` should read `/app/lines.txt` and write `/app/nospaces.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
