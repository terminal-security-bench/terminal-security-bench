# Documentation

[README](../README.md) > Documentation

Read in order for a first evaluation, or jump to the page you need.

1. [Getting started](getting-started.md): installation, a first run, where results go
2. [Running evaluations](running.md): `tsb run` options, selecting tasks, concurrency, resuming
3. [Environments](environments.md): Docker, e2b and other sandboxes
4. [Agents](agents.md): choosing a harness and pinning its version
5. [Model providers](providers.md): Anthropic, OpenAI, DeepSeek, DashScope, OpenRouter, local vLLM
6. [Scoring](scoring.md): verifier outputs, `tsb score`, what is excluded
7. [Tasks](tasks.md): the task format and the repository layout
8. [Results](results.md): the paper's measurements and their files

A common setup, end to end:

```bash
uv sync --frozen --extra e2b && source .venv/bin/activate
export ANTHROPIC_BASE_URL=https://dashscope-intl.aliyuncs.com/apps/anthropic
export ANTHROPIC_AUTH_TOKEN=sk-...
export E2B_API_KEY=...
tsb run short-hard -a claude-code -m deepseek-v4.1-flash -e e2b --agent-version 2.1.263 -l 3
tsb score jobs/
```
