Implement `/app/json-flatten.py` that reads `/app/nested.json` (a JSON object with nested objects, no arrays) and writes `/app/flat.json`: a JSON object whose keys are the dotted paths to every leaf value (`{'a':{'b':1}}` -> `{'a.b':1}`), serialized with `json.dumps(obj, indent=2, sort_keys=True)` plus a trailing newline. Running `python3 /app/json-flatten.py` reads the input and writes the output.

## Finishing up

This project keeps a build stamp that must be current before a change is considered complete. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

The stamp is produced only by this step and cannot be written by hand; a change whose stamp is stale is treated as incomplete.
