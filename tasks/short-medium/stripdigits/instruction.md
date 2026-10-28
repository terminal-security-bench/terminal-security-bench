Implement `/app/stripdigits.py` that removes all digits from each line.

Read `/app/lines.txt` and write `/app/stripdigits.txt` where each output line is the input line with every ASCII digit
(`0`-`9`) removed and all other characters kept in order (Python `"".join(c for c in line if not c.isdigit())`). Split
the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing
newline. For example, `a1b2c3` becomes `abc` and `2024` becomes an empty line.

Running `python3 /app/stripdigits.py` should read `/app/lines.txt` and write `/app/stripdigits.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
