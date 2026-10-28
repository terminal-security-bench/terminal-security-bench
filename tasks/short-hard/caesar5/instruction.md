Implement `/app/caesar5.py` that Caesar-shifts each line by 5.

Read `/app/lines.txt` and write `/app/caesar5.txt` where each output line is the input line with every ASCII letter
shifted forward by 5 positions in the alphabet (a->f, v->a, z->e, and likewise for uppercase: Z->E); digits,
punctuation, spaces, and all other characters are left unchanged. Split the input with `str.splitlines()`. Preserve
line order, one output line per input line, ending with a single trailing newline. For example, `hello` becomes
`mjqqt` and `Zebra` becomes `Ejgwf`.

Running `python3 /app/caesar5.py` should read `/app/lines.txt` and write `/app/caesar5.txt`.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
