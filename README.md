# TerminalSecurityBench

**Security evaluation of terminal agents under third-party prompt injection, in Harbor format.**

[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Format: Harbor](https://img.shields.io/badge/format-Harbor-6f42c1.svg)](https://harborframework.com)

A terminal agent reads files, runs commands and installs dependencies while it works on a task.
Some of what it reads is written by third parties: a README, a configuration file, a helper script
or a compiled dependency. TerminalSecurityBench measures what happens when that content asks the
agent to do something the user did not ask for.

Each task pairs a benign request with a planted attack, and every trial gets two deterministic
scores, with no model judge:

- **Utility**: whether the agent completed the user's task, checked by the task's own tests.
- **Attack success**: whether it performed the planted action, checked from the container state
  after the agent exits.

## 📦 Benchmark

A suite combines a task **split** with a **threat level**. The short split contains authored
tasks; the long split is derived from Terminal-Bench 2.1. Every base task appears at all three
threat levels, so a difference between levels reflects the attack, not the task. The benign
control contains the short tasks without any planted attack.

| Suite | Tasks | Attacks |
| --- | ---: | ---: |
| `short-easy` | 183 | 366 |
| `short-medium` | 183 | 366 |
| `short-hard` | 183 | 366 |
| `long-easy` | 89 | 309 |
| `long-medium` | 89 | 388 |
| `long-hard` | 89 | 267 |
| `short-benign` | 183 | 0 |

| Threat level | Where the attack is planted |
| --- | --- |
| 🟢 EASY | Untrusted task content asks for the sensitive action directly |
| 🟡 MEDIUM | A readable dependency of the task performs the sensitive action |
| 🔴 HARD | A compiled dependency the task requires performs the sensitive action |

## 🚀 Quick start

Requirements: Docker, Python 3.12 or later, and [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/terminal-security-bench/terminal-security-bench.git
cd terminal-security-bench
uv sync --frozen
source .venv/bin/activate

tsb list                                   # the suites and their sizes
tsb run short-easy -a oracle -l 2          # reference solutions: checks your Docker setup

export ANTHROPIC_API_KEY=...
tsb run short-hard -a claude-code -m anthropic/claude-opus-5-5 -l 1
tsb score jobs/
```

Model calls and environment builds may incur provider charges. Tasks run the scripts and binaries
they ship, so run them only in disposable environments.

## 📚 Documentation

| Page | What it covers |
| --- | --- |
| [Getting started](docs/getting-started.md) | Installation, a first run, where results go |
| [Running evaluations](docs/running.md) | `tsb run` options, selecting tasks, concurrency, resuming |
| [Environments](docs/environments.md) | Docker, e2b and other sandboxes |
| [Agents](docs/agents.md) | Choosing a harness and pinning its version |
| [Model providers](docs/providers.md) | Anthropic, OpenAI, DeepSeek, DashScope, OpenRouter, local vLLM |
| [Scoring](docs/scoring.md) | Verifier outputs, `tsb score`, what is excluded |
| [Tasks](docs/tasks.md) | The task format and the repository layout |
| [Results](docs/results.md) | The paper's measurements and their files |

## ⚖ License

The code and the authored task material are released under the [Apache License 2.0](LICENSE).
Long-split tasks keep their upstream attribution and notices; see [NOTICE](NOTICE) and each
task's `MODIFICATIONS.md` for the changes made to Terminal-Bench 2.1. The task data carries
training-contamination canaries; keep them when redistributing it.

## 📝 Citation

```bibtex
@misc{tsb2026,
  title  = {TerminalSecurityBench: The Security Frontier of Terminal Agents},
  author = {Anonymous},
  year   = {2026},
  note   = {Under review}
}
```
