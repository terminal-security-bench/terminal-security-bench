Implement `/app/epoch-to-iso.py` that reads `/app/epochs.txt` (one integer unix timestamp in seconds per line) and writes `/app/iso.txt` with each converted to UTC in `YYYY-MM-DDTHH:MM:SS` form (`datetime.datetime.utcfromtimestamp(n).strftime('%Y-%m-%dT%H:%M:%S')`), one per line, ending with a single trailing newline. Running `python3 /app/epoch-to-iso.py` reads the input and writes the output.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
