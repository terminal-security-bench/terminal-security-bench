# Results

[README](../README.md) > Results | Previous: [Tasks](tasks.md)

The tables below are the measurements reported in the paper. Each task instance was run once per
agent and defense.

**Frontier agents, no defense.** Each cell is utility / ASR in percent.

| Agent model | EASY short | EASY long | MEDIUM short | MEDIUM long | HARD short | HARD long |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Opus-5.5 | 98.9 / 0.0 | 91.4 / 3.6 | 97.9 / 9.6 | 90.7 / 6.4 | 61.9 / 63.8 | 53.8 / 99.2 |
| Opus-4.8 | 97.8 / 0.0 | 78.7 / 5.2 | 95.6 / 86.3 | 77.5 / 2.3 | 88.8 / 89.4 | 52.3 / 90.9 |
| GPT-6.1-Sol | 97.8 / 0.0 | 84.1 / 16.3 | 95.6 / 38.5 | 75.3 / 15.7 | 97.2 / 98.6 | 46.1 / 92.1 |
| GPT-5.6-Sol | 95.1 / 90.7 | 82.0 / 41.7 | 94.5 / 83.3 | 78.7 / 52.8 | 98.3 / 100.0 | 50.6 / 95.9 |
| Kimi-K3 | 95.6 / 1.6 | 82.0 / 16.5 | 94.5 / 48.1 | 83.1 / 11.3 | 95.0 / 96.1 | 51.7 / 96.3 |
| GLM-5.3 | 96.7 / 0.0 | 83.1 / 9.4 | 96.7 / 16.9 | 80.7 / 4.2 | 84.2 / 83.6 | 47.2 / 83.9 |
| DeepSeek-V4.1-Flash | 97.8 / 0.0 | 88.8 / 10.4 | 96.2 / 20.8 | 87.6 / 15.2 | 62.5 / 61.9 | 52.8 / 95.1 |
| Qwen3.8-Max-0902 | 96.0 / 0.0 | 81.5 / 6.8 | 96.7 / 15.5 | 80.2 / 2.0 | 84.4 / 86.8 | 46.3 / 91.9 |

**Small models under each defense.** Each cell is utility / ASR in percent.

| Agent model | Defense | EASY short | EASY long | MEDIUM short | MEDIUM long | HARD short | HARD long |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Qwen3.6-27B | None | 94.5 / 70.5 | 43.8 / 58.3 | 94.0 / 87.4 | 49.4 / 73.5 | 98.4 / 100.0 | 33.0 / 86.4 |
| Qwen3.6-27B | Fides | 98.4 / 0.0 | 45.7 / 32.9 | 95.1 / 88.3 | 36.0 / 63.0 | 97.8 / 100.0 | 40.6 / 91.3 |
| Qwen3.6-27B | Spotlighting | 97.3 / 46.2 | 46.1 / 56.6 | 95.1 / 88.8 | 40.4 / 76.8 | 98.4 / 100.0 | 39.1 / 92.0 |
| Qwen3.6-27B | Struq | 95.0 / 59.4 | 48.3 / 51.1 | 95.1 / 80.9 | 46.1 / 68.3 | 97.8 / 100.0 | 37.1 / 88.8 |
| Qwen3.6-35B-A3B | None | 93.4 / 87.7 | 39.1 / 54.0 | 93.4 / 98.6 | 33.3 / 73.4 | 98.9 / 100.0 | 33.3 / 94.3 |
| Qwen3.6-35B-A3B | Fides | 95.1 / 89.9 | 34.1 / 47.8 | 94.5 / 98.4 | 42.7 / 69.2 | 97.8 / 100.0 | 32.1 / 84.6 |
| Qwen3.6-35B-A3B | Spotlighting | 95.1 / 49.7 | 32.2 / 47.4 | 94.5 / 90.2 | 37.9 / 74.9 | 96.7 / 100.0 | 31.0 / 94.3 |
| Qwen3.6-35B-A3B | Struq | 96.2 / 81.4 | 37.9 / 49.7 | 95.1 / 97.3 | 47.1 / 74.1 | 96.2 / 100.0 | 31.0 / 94.3 |

## Files

Every table the paper reports is in [`metadata/evaluation/`](../metadata/evaluation/):

| File | Content |
| --- | --- |
| [`measurements.csv`](../metadata/evaluation/measurements.csv) | Utility and ASR per model, defense, threat level and split |
| [`attack_verdicts.csv`](../metadata/evaluation/attack_verdicts.csv) | One row per planted attack and agent run, with its outcome and labels |
| [`asr_by_level.csv`](../metadata/evaluation/asr_by_level.csv) | ASR per threat level, pooled and per attack family |
| [`benign_utility.csv`](../metadata/evaluation/benign_utility.csv) | Utility on the benign short split |
| [`external_benchmarks.csv`](../metadata/evaluation/external_benchmarks.csv) | Utility and ASR of the same agents on six existing benchmarks |
| [`injection_channel.csv`](../metadata/evaluation/injection_channel.csv) | ASR of one payload delivered through seven channels |
| [`binary_ablation.csv`](../metadata/evaluation/binary_ablation.csv) | One attack as a readable script and as a compiled binary |
| [`recognition_census.csv`](../metadata/evaluation/recognition_census.csv) | ASR split by whether the agent recognised the threat |
| [`disguise.csv`](../metadata/evaluation/disguise.csv) | One exfiltration under a suspicious and a neutral wording |
| [`technique_pooled_vs_controlled.csv`](../metadata/evaluation/technique_pooled_vs_controlled.csv) | ASR per attack technique, pooled and within level and split; * marks a rate over fewer than 30 attacks |
| [`technique_by_model_hard_long.csv`](../metadata/evaluation/technique_by_model_hard_long.csv) | ASR per attack technique and model at HARD on the long split; * marks a rate over fewer than 30 attacks |
| [`taxonomy_distribution.csv`](../metadata/evaluation/taxonomy_distribution.csv) | Attacks per label in each public standard |
| [`fides_blocked.csv`](../metadata/evaluation/fides_blocked.csv) | Commands the Fides defense withheld, by reason |
| [`turns.csv`](../metadata/evaluation/turns.csv) | Mean agent turns per model, threat level and split |
| [`construction_rounds.csv`](../metadata/evaluation/construction_rounds.csv) | Distinct tasks per round of the construction loop |
| [`model_harness.csv`](../metadata/evaluation/model_harness.csv) | Model, harness and harness version of every agent |
