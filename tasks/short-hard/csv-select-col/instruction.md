Implement `/app/csv-select-col.py` that reads `/app/data.csv` (a header row then data rows, comma-separated, no embedded commas) and writes `/app/names.txt` with the value of the `name` column for each data row, in order, one per line, ending with a single trailing newline. Use `csv.DictReader`. Running `python3 /app/csv-select-col.py` reads the input and writes the output.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
