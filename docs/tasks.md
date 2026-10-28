# Tasks

[README](../README.md) > Tasks | Previous: [Scoring](scoring.md) | Next: [Results](results.md)

Every task is a directory in [Harbor's task format](https://harborframework.com): a request for the
agent, a container definition, tests, and a reference solution. Harbor reads it directly, so a task
also runs without `tsb`:

```bash
harbor run -p tasks/short-easy -a claude-code -m anthropic/claude-opus-5-5 -n 1
```

## One task

```text
tasks/<suite>/<task>/
  instruction.md          the user's request, which is all the agent is told
  task.toml               Harbor configuration: timeouts and container resources
  environment/
    Dockerfile            builds the container, including the planted files
    planted/              files the Dockerfile copies in, where a task has them
  tests/
    test.sh               Harbor's verifier entry point
    test_outputs.py       utility: did the agent do the task (writes reward.txt)
    security_check.py     security: did a planted attack run (writes security.json)
    footprints.py         the state checks security_check.py applies
    attack.json           the planted attacks and their labels
  solution/solve.sh       the reference solution, run by the `oracle` agent
```

Long-split tasks also keep a `MODIFICATIONS.md` that lists what changed from the Terminal-Bench 2.1
original.

## Suites and the registry

`tasks/<suite>/` holds one suite. [`registry.json`](../registry.json) defines the suites as Harbor
datasets with paths relative to this repository, so a checkout can be used as a dataset source.

## Repository layout

```text
tasks/<suite>/<task>/     the tasks, as above
metadata/
  attacks.csv             every planted attack, its check and its labels in public standards
  source_task_hashes.csv  hashes of the original Terminal-Bench 2.1 task trees
  evaluation/             the measurements reported in the paper (see Results)
  files.json              size, mode and SHA-256 of every file in the release
registry.json             Harbor dataset definitions
src/tsb/                  the `tsb` command line tool and scorer
tests/                    tests of `tsb`
docs/                     these pages
```

`metadata/files.json` lets a copy be checked against the release byte for byte.

## Safety

Tasks run the scripts and binaries they ship, and some of them are attacks by design. Run them only
in disposable environments such as the containers Harbor creates, never on a machine that holds
real credentials.
