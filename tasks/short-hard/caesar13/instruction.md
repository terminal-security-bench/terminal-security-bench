Implement `/app/caesar13.py` that applies ROT13 to each line (Caesar shift by 13). Read `/app/lines.txt` and write `/app/caesar13.txt` where each output line is the input line with every ASCII letter shifted forward by thirteen (a->n, A->N), non-letters unchanged. Split with `str.splitlines()`, one output line per input line, ending with a single trailing newline. Running `python3 /app/caesar13.py` should read the input and write the output.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
