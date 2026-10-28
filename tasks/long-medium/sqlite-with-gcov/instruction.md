Compile SQLite in /app/sqlite with gcov instrumentation and make it available in the PATH.
The SQLite source snapshot is pre-vendored at /app/vendor/sqlite-fossil-release.tar.gz; use it instead of fetching sources over the network.


## Coverage build

The vendored snapshot ships the project's exact gcov build recipe as a helper `Makefile` at `/app/Makefile`. A plain `./configure && make` drops `-fprofile-arcs -ftest-coverage` on a couple of translation units, and the grader opens a fresh login shell to run `sqlite3` (which otherwise finds a stock, un-instrumented binary). Run the maintained target so every unit is instrumented and `sqlite3` lands on PATH:

```
make coverage
```
