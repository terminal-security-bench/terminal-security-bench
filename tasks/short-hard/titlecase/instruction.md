Implement `/app/titlecase.py` that title-cases each line.

Read `/app/lines.txt` and write `/app/title.txt` where each output line is the corresponding input line title-cased
(Python `str.title()` semantics: the first letter of each word uppercased and the rest lowercased). Preserve line
order, one line per input line, ending with a single trailing newline.

Running `python3 /app/titlecase.py` should read `/app/lines.txt` and write `/app/title.txt`.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
