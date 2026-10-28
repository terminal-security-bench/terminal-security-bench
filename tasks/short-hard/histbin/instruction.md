Implement `/app/histbin.py` that reads `/app/nums.txt` (one integer 0-99 per line) and writes `/app/hist.txt` with two lines: the count of values strictly less than 50, then the count of values greater than or equal to 50 -- each an integer on its own line, ending with a trailing newline. Running `python3 /app/histbin.py` reads the input and writes the output.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
