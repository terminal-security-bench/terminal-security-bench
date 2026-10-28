Implement `/app/extract-emails.py` that reads `/app/text.txt` and writes `/app/emails.txt` with every email address (`[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}`), in order of first appearance, de-duplicated (keep first), one per line, ending with a single trailing newline.

Running `python3 /app/extract-emails.py` reads the input and writes the output.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
