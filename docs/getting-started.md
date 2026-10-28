# Getting started

[README](../README.md) > Getting started | Next: [Running evaluations](running.md)

TerminalSecurityBench is a set of [Harbor](https://harborframework.com) tasks plus `tsb`, a small
command line tool that runs them through Harbor and scores the results. Harbor builds each task's
container, installs the agent inside it, runs the agent, then runs the task's verifier.

## Requirements

- Docker, for the default environment. A cloud sandbox can be used instead; see
  [Environments](environments.md).
- Python 3.12 or later and [uv](https://docs.astral.sh/uv/).
- An API key or an endpoint for the model under test; see [Model providers](providers.md).

## Install

```bash
git clone https://github.com/terminal-security-bench/terminal-security-bench.git
cd terminal-security-bench
uv sync --frozen            # Harbor and tsb, at the versions in uv.lock
source .venv/bin/activate   # puts `tsb` and `harbor` on PATH
```

`uv sync --frozen` installs exactly the locked versions, including Harbor itself. Cloud
environments are optional extras, for example `uv sync --frozen --extra e2b`.

## Check the setup without a model

Harbor's `oracle` agent runs each task's reference solution instead of a model. It costs nothing
and shows that Docker can build the environments and that the tests pass:

```bash
tsb list                          # the suites and their sizes
tsb run short-easy -a oracle -l 2
```

Every trial should report a reward of 1.0.

## A first run with a model

```bash
export ANTHROPIC_API_KEY=...
tsb run short-hard -a claude-code -m anthropic/claude-opus-5-5 -l 1
tsb score jobs/
```

- `-a` picks the agent harness ([Agents](agents.md)) and `-m` the model
  ([Model providers](providers.md)).
- `-l 1` runs one task; drop it to run the whole suite.
- `tsb run` prints the Harbor command it executes, so every run can be reproduced from that line.

## Where results go

Each run is a Harbor job under `jobs/<job name>/`, one directory per trial:

```text
jobs/<job>/
  result.json                 the job summary
  <task>__<id>/
    result.json               the trial: agent, model, versions, tokens, timing, exceptions
    agent/                    the agent's own logs and trajectory
    verifier/reward.txt       utility, 0 or 1
    verifier/security.json    one verdict per planted attack
```

`tsb score` reads these directories; see [Scoring](scoring.md). Keep the whole job directory when
you archive or share an evaluation.

## Development

```bash
uv sync --frozen --extra dev
uv run pytest
```

The tests use synthetic Harbor result directories and build commands without starting an agent.
