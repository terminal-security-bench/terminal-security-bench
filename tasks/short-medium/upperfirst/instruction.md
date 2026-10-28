Implement `/app/upperfirst.py` that capitalizes the first character of each line.

Read `/app/lines.txt` and write `/app/upperfirst.txt` where each output line is the corresponding input line with only
its first character upper-cased (the rest of the line left unchanged; Python `line[:1].upper() + line[1:]`). Preserve
line order, one line per input line, ending with a single trailing newline.

Running `python3 /app/upperfirst.py` should read `/app/lines.txt` and write `/app/upperfirst.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
