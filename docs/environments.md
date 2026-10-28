# Environments

[README](../README.md) > Environments | Previous: [Running evaluations](running.md) |
Next: [Agents](agents.md)

An environment is where a task's container runs. Harbor builds it from the task's
`environment/Dockerfile`; only public base images and the task's own files are needed, so no image
has to be downloaded from this repository. Choose it with `tsb run -e <name>`.

| Environment | Install | Credentials | Notes |
| --- | --- | --- | --- |
| `docker` (default) | nothing extra | none | Builds and runs on the local Docker daemon |
| `e2b` | `uv sync --frozen --extra e2b` | `E2B_API_KEY` | Builds an [e2b](https://e2b.dev) template per task environment |
| `daytona` | `uv sync --frozen --extra daytona` | see Harbor's documentation | [Daytona](https://daytona.io) sandboxes |
| `modal` | `uv sync --frozen --extra modal` | see Harbor's documentation | [Modal](https://modal.com) sandboxes |

Harbor supports further environments (`harbor run --help` lists them under `--env`). Their
packages come from Harbor's own extras, for example `uv pip install 'harbor[runloop]==0.24.0'`.

## Docker

```bash
tsb run short-hard -a claude-code -m anthropic/claude-opus-5-5
```

- The first run of a task builds its image; later trials of the same task reuse the cached layers.
- Harbor removes the images it built when a trial ends. Base images it pulled, such as
  `python:3.13-slim-bookworm` and the Terminal-Bench 2.1 images of the long split, stay cached.
- The long split pulls one public image per task from Docker Hub. Docker Hub limits anonymous
  pulls per IP address; `docker login` raises the limit.
- The agent runs inside the task's container. A model endpoint on the host is reached through the
  host's address on the Docker network, not `localhost`; see
  [Model providers](providers.md#a-local-vllm-server).
- A container limited to a few CPUs still reports every core of the host. Each task's
  `[environment.env]` sets the thread counts of PyTorch, OpenMP, BLAS and build tools to its `cpus`
  in every environment. `tsb run` also caps processes, swap and open files on Docker
  (`src/tsb/limits.py`); `harbor run` called directly does not.

## e2b

```bash
uv sync --frozen --extra e2b
export E2B_API_KEY=...
tsb run short-hard -a claude-code -m anthropic/claude-opus-5-5 -e e2b
```

- Harbor turns each task's Dockerfile into an e2b template on your account the first time the task
  runs there, so the first trial of a task takes longer.
- The model endpoint must be reachable from the internet, because the agent runs in e2b's cloud.
- Concurrency (`-n`) is bounded by the number of sandboxes your e2b plan allows at once.

## Tasks that use online sources

Many long tasks install packages or query online services while they are solved or verified, so a
later change in one of those sources can break a task that worked before.

## Choosing

| If you want | Use |
| --- | --- |
| No cloud account, full control of the machine | `docker` |
| Many trials at once without local CPU and disk | `e2b` (or another cloud environment) |
| A reproducible comparison between agents | the same environment for every agent |
