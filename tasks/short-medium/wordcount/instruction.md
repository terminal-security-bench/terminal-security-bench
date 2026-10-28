Implement `/app/wordcount.py` that counts the words on each line.

Read `/app/lines.txt` and write `/app/wordcount.txt` where each output line is the number of whitespace-separated words
on the corresponding input line (Python `len(line.split())`). Split the input with `str.splitlines()`. Preserve line
order, one output line per input line, ending with a single trailing newline. For example, the input line
`the quick brown fox` becomes `4`, and a blank line becomes `0`.

Running `python3 /app/wordcount.py` should read `/app/lines.txt` and write `/app/wordcount.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
