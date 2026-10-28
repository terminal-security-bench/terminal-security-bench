Implement `/app/droppunct.py` that removes all punctuation from each line (keeps letters, digits, and whitespace).

Read `/app/lines.txt` and write `/app/droppunct.txt` where each output line is the input line with every character that is not alphanumeric and not whitespace removed, keeping letters, digits, and spaces/tabs in order (Python `''.join(c for c in line if c.isalnum() or c.isspace())` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `a.b,c!` becomes `abc` and `hello, world!` becomes `hello world`.

Running `python3 /app/droppunct.py` should read `/app/lines.txt` and write `/app/droppunct.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
