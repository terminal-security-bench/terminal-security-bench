# Agents

[README](../README.md) > Agents | Previous: [Environments](environments.md) |
Next: [Model providers](providers.md)

The agent, or harness, is the program that drives the model inside the task's container. The
benchmark ships no harness of its own: `tsb run -a <name>` selects one of Harbor's built-in agents,
and Harbor installs it into the container when the trial starts.

## Choosing a harness

| `-a` | Harness | Model API it speaks |
| --- | --- | --- |
| `claude-code` | Claude Code | Anthropic Messages |
| `codex` | Codex CLI | OpenAI Responses |
| `opencode` | OpenCode | per provider |
| `mini-swe-agent` | mini-SWE-agent | OpenAI-compatible, through LiteLLM |
| `oracle` | the task's reference solution, no model | none |

Harbor 0.24.0 has more (`gemini-cli`, `aider`, `goose`, `openhands`, `terminus-2` and others);
`harbor run --help` lists every name under `--agent`. How each harness reaches a model is on
[Model providers](providers.md).

The paper's agents used `claude-code` and `codex`;
[`metadata/evaluation/model_harness.csv`](../metadata/evaluation/model_harness.csv) lists the
harness and version of each.

## Pinning the agent version

Without a version, Harbor installs the newest release of the harness when each trial starts, so
two runs a week apart may test different agents. Pin it for any comparison:

```bash
tsb run short-hard -a claude-code -m anthropic/claude-opus-5-5 --agent-version 2.1.263
tsb run short-hard -a codex -m openai/gpt-6.1-sol --agent-version 0.153.4
```

- `--agent-version` is passed to Harbor as `--ak version=<version>`; the harness installs that
  release (for example `npm install -g @anthropic-ai/claude-code@2.1.263`).
- The installed version is recorded in each trial's `result.json` under `agent_info.version`.
  Check it there rather than assuming it.
- The Harbor version itself is pinned by `uv.lock` (0.24.0) and installed by `uv sync --frozen`.

## Agent arguments and environment

Further harness settings go to Harbor after `--`:

```bash
# A Harbor agent argument (repeatable).
tsb run short-hard -a claude-code -m anthropic/claude-opus-5-5 -- --ak <key>=<value>

# An environment variable for the agent only.
tsb run short-hard -a claude-code -m anthropic/claude-opus-5-5 -- --ae <NAME>=<value>
```

The arguments each harness accepts are documented with Harbor's agents.
