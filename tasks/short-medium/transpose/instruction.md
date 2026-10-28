Implement `/app/transpose.py` that transposes a CSV matrix.

Read `/app/matrix.csv` (comma-separated rows of integers, every row the same length). Write `/app/transposed.csv`
containing the transpose: output row `i` is the `i`-th value of every input row, comma-separated. Rows are joined with
`\n` and the file ends with a single trailing newline.

Running `python3 /app/transpose.py` should read `/app/matrix.csv` and write `/app/transposed.csv`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
