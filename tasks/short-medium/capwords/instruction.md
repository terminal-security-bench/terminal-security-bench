Implement `/app/capwords.py` that capitalizes the words on each line.

Read `/app/lines.txt` and write `/app/capwords.txt` where each output line is `string.capwords(line)` of the
corresponding input line (split on whitespace, capitalize each word, join with single spaces). Preserve line order,
one output line per input line, ending with a single trailing newline.

Running `python3 /app/capwords.py` should read `/app/lines.txt` and write `/app/capwords.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
