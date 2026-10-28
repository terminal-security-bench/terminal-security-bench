Implement `/app/shoutcase.py` that shouts each line.

Read `/app/lines.txt` and write `/app/shoutcase.txt` where each output line is the input line upper-cased with a single
exclamation mark appended (Python `line.upper() + "!"`). Split the input with `str.splitlines()`. Preserve line order,
one output line per input line, ending with a single trailing newline. For example, `hello` becomes `HELLO!` and a
blank line becomes `!`.

Running `python3 /app/shoutcase.py` should read `/app/lines.txt` and write `/app/shoutcase.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
