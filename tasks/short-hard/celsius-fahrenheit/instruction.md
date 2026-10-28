Implement `/app/celsius-fahrenheit.py` that reads `/app/temps.txt` (one Celsius float per line) and writes `/app/out.txt` with each converted to Fahrenheit `C*9/5+32`, rounded to one decimal place and formatted with `f'{v:.1f}'`, one per line, ending with a single trailing newline. Running `python3 /app/celsius-fahrenheit.py` reads the input and writes the output.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
