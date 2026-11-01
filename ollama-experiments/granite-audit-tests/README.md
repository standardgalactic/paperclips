# Granite audit experiments

Requires Python 3.9+ and a running local Ollama server with the model already installed. No Python packages are needed. The runner never executes model output or downloads models.

Run the six cases independently and once in a batch (seven calls):

```bash
bash run.sh --models granite4.1:3b
```

Compare models across three seeds:

```bash
bash run.sh --models granite4.1:3b granite4.1:8b --seeds 42 43 44
```

Each request starts a fresh conversation. All inputs, prompts, readable responses, raw API responses, settings, scores, timings, and the Python-computed answer key are saved under a unique timestamped directory in `audit-runs/`. Summaries are updated after every request. Failures are recorded and remaining cases continue. Request errors cause a nonzero exit; wrong model answers are recorded in scores.

Default JSON outputs are checked for sums, claim correctness, budget compliance, signed remainders, missing cases, duplicate cases, extra cases, and value types. Formatting failures are separate from wrong field values. Inspect malformed outputs manually before drawing conclusions. A `done_reason` of `length` suggests truncation; increase `--tokens` before interpreting it as a reasoning failure.

Compare the original prose style with:

```bash
bash run.sh --models granite4.1:3b --style prose
```

Prose responses require manual review against the saved answer key. JSON introduces an additional formatting constraint and may change performance. Use `--shuffle` to shuffle batch order deterministically by seed, `--mode single` or `--mode batch` to isolate conditions, and `--dry-run` to save prompts without contacting Ollama. Defaults: temperature 0.3, seed 42, 3,000 output tokens, 8,192-token context, 600-second request timeout. Shared seeds do not equate random samples across models. Record Ollama version, installed model details, and hardware when comparing runs. Timing includes loading and transport.

The fixed cases are a small diagnostic, not a broad benchmark. Repeating seeds tests variability on these inputs, not generalization. Earlier observations are in `prior-results/observations.md`; incomplete material is unassessed. No new Granite runs were performed while preparing this suite.

Check the harness with:

```bash
python3 -m unittest -v test_runner.py
```

The checks validate scoring, arithmetic, malformed and incomplete responses, type errors, and HTTP behavior with a mock server. `harness-validation.txt` contains the preparation results. The previous planning, essay, and screenplay runner is preserved under `writing-experiments/`.
