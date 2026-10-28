# Model providers

[README](../README.md) > Model providers | Previous: [Agents](agents.md) |
Next: [Scoring](scoring.md)

A harness reaches its model through the environment variables it already reads. Harbor forwards
those variables from your shell into the task's container, so setting them before `tsb run` is
all the configuration needed. Any endpoint that speaks the harness's API works: the vendor's own
API, a router, or a server you run.

## What each harness reads

| Harness | API key | Endpoint | `-m` |
| --- | --- | --- | --- |
| `claude-code` | `ANTHROPIC_API_KEY`, or `ANTHROPIC_AUTH_TOKEN` for a bearer token | `ANTHROPIC_BASE_URL` (Anthropic Messages) | `anthropic/<model>`; with a custom endpoint, the endpoint's own model id |
| `codex` | `OPENAI_API_KEY` | `OPENAI_BASE_URL` (OpenAI Responses) | `openai/<model>`; the part after the last `/` is sent |
| `mini-swe-agent` | `MSWEA_API_KEY`, or the provider's own key variable | `OPENAI_BASE_URL` | a [LiteLLM](https://docs.litellm.ai/docs/providers) model name |

A variable can also be given to the agent alone with `-- --ae NAME=value` (see
[Agents](agents.md#agent-arguments-and-environment)).

With `claude-code` and a custom `ANTHROPIC_BASE_URL`, `-m` is sent as written, so give the
model id the endpoint expects (for example `-m deepseek-v4.1-flash`, not
`-m anthropic/deepseek-v4.1-flash`).

## Anthropic

```bash
export ANTHROPIC_API_KEY=sk-ant-...
tsb run short-hard -a claude-code -m anthropic/claude-opus-5-5
```

## OpenAI

```bash
export OPENAI_API_KEY=sk-...
tsb run short-hard -a codex -m openai/gpt-6.1-sol
```

## DeepSeek

DeepSeek serves an Anthropic-compatible endpoint for Claude Code:

```bash
export ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
export ANTHROPIC_AUTH_TOKEN=sk-...          # a DeepSeek API key
unset ANTHROPIC_API_KEY                     # Harbor reads it before ANTHROPIC_AUTH_TOKEN
tsb run short-hard -a claude-code -m deepseek-flash
```

## Alibaba Cloud Model Studio (DashScope)

DashScope serves an Anthropic-compatible endpoint, and its model list includes models from several
vendors.

| Region | `ANTHROPIC_BASE_URL` | `OPENAI_BASE_URL` |
| --- | --- | --- |
| International (Singapore) | `https://dashscope-intl.aliyuncs.com/apps/anthropic` | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` |
| China (Beijing) | `https://dashscope.aliyuncs.com/apps/anthropic` | `https://dashscope.aliyuncs.com/compatible-mode/v1` |

```bash
export ANTHROPIC_BASE_URL=https://dashscope-intl.aliyuncs.com/apps/anthropic
export ANTHROPIC_AUTH_TOKEN=sk-...          # a DashScope API key
unset ANTHROPIC_API_KEY                     # Harbor reads it before ANTHROPIC_AUTH_TOKEN
tsb run short-hard -a claude-code -m deepseek-v4.1-flash

# codex, through the OpenAI-compatible endpoint (Responses API)
export OPENAI_BASE_URL=https://dashscope-intl.aliyuncs.com/compatible-mode/v1
export OPENAI_API_KEY=sk-...                # a DashScope API key
tsb run short-hard -a codex -m openai/deepseek-v4.1-flash
```

## OpenRouter

```bash
# claude-code, through OpenRouter's Anthropic-compatible endpoint
export ANTHROPIC_BASE_URL=https://openrouter.ai/api
export ANTHROPIC_AUTH_TOKEN=sk-or-...
unset ANTHROPIC_API_KEY                     # Harbor reads it before ANTHROPIC_AUTH_TOKEN, even when empty
tsb run short-hard -a claude-code -m <vendor>/<model>

# codex, through its OpenAI-compatible endpoint
export OPENAI_BASE_URL=https://openrouter.ai/api/v1
export OPENAI_API_KEY=sk-or-...
tsb run short-hard -a codex -m <vendor>/<model>
```

## A local vLLM server

[vLLM](https://docs.vllm.ai) serves an OpenAI-compatible API, including Responses, and an
Anthropic Messages endpoint, from the same server:

```bash
vllm serve <model> --host 0.0.0.0 --port 8000 --served-model-name my-model
```

The agent runs inside the task's container, not on the host, so the endpoint must be an address
the container can reach:

- With Docker on the same machine, use the host's address on the Docker network (often
  `172.17.0.1`; `ip addr show docker0` prints it), not `localhost`.
- With a cloud environment such as e2b, the server must be reachable from the internet.

```bash
# claude-code
export ANTHROPIC_BASE_URL=http://172.17.0.1:8000
export ANTHROPIC_API_KEY=unused             # vLLM accepts any key unless started with --api-key
tsb run short-hard -a claude-code -m my-model

# codex
export OPENAI_BASE_URL=http://172.17.0.1:8000/v1
export OPENAI_API_KEY=unused
tsb run short-hard -a codex -m openai/my-model
```

Serve the model with the tool-call and reasoning parsers its card recommends; an agent cannot work
without tool calls.

## Costs

`result.json` reports token counts for each trial. Its `cost_usd` is the harness's own estimate,
not the provider's bill: `claude-code` prices tokens as it would for Anthropic's models, whatever
model actually served them. Use the provider's billing for the real cost.
