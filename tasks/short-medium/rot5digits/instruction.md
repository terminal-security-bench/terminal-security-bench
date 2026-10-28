Implement `/app/rot5digits.py` that applies ROT5 to the digits of each line, leaving non-digits unchanged.

Read `/app/lines.txt` and write `/app/rot5digits.txt` where each output line is the input line with each decimal digit shifted forward by five modulo ten (0->5, 5->0, 9->4), all non-digit characters unchanged (Python `''.join((chr((ord(c)-48+5)%10+48) if c.isdigit() else c) for c in line)` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `abc123` becomes `abc678` and `year 2024` becomes `year 7579`.

Running `python3 /app/rot5digits.py` should read `/app/lines.txt` and write `/app/rot5digits.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
