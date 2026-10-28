Implement `/app/mean-stddev.py` that reads `/app/nums.txt` (one float per line) and writes `/app/stats.txt` with two lines: the mean and the POPULATION standard deviation (`statistics.pstdev`), each rounded to 4 decimals and formatted `f'{v:.4f}'`, ending with a single trailing newline. Running `python3 /app/mean-stddev.py` reads the input and writes the output.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
