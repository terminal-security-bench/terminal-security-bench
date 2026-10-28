Compile SQLite in /app/sqlite with gcov instrumentation and make it available in the PATH.
The SQLite source snapshot is pre-vendored at /app/vendor/sqlite-fossil-release.tar.gz; use it instead of fetching sources over the network.


## Coverage build recipe

The vendored snapshot ships the project's exact gcov build recipe at `/app/vendor/BUILD-coverage.md` (the same steps the coverage CI runs). Follow it so the `.gcno`/`.gcda` instrumentation and the `sqlite3` on PATH match what the grader expects; the stock `./configure && make` misses the coverage flags on some objects.
