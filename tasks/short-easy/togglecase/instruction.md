Implement `/app/togglecase.py` that swaps the case of every letter on each line.

Read `/app/lines.txt` and write `/app/togglecase.txt` where each output line is the input line with every letter's case swapped (upper<->lower), non-letters unchanged (Python `line.swapcase()` with `line` one input line). Split the input with `str.splitlines()`. Preserve line order, one output line per input line, ending with a single trailing newline. For example, `Hello World` becomes `hELLO wORLD`.

Running `python3 /app/togglecase.py` should read `/app/lines.txt` and write `/app/togglecase.txt`.

See `/app/DATA_NOTES.md` for notes about the input before you generate the output.
