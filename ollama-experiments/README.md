# Small Ollama experiments

Requires Python 3.9+ and a running local Ollama server with your model already installed. No Python packages are needed. This runner calls the local HTTP API and never executes generated text or code. It does not download models. If Ollama is not running, start it in another terminal with `ollama serve`.

From this directory, try one planning experiment first:

```bash
bash run.sh --model granite4.1:3b --task plan
```

Run all three paired experiments on each model:

```bash
bash run.sh --model granite4.1:3b
bash run.sh --model granite4.1:8b
```

Inspect prompts without contacting Ollama:

```bash
bash run.sh --dry-run
```

The planning task asks for an implementable six-hour notes application plan, then cuts the budget and changes storage. The essay uses a supplied fictional evidence set, then corrects one observation. The screenplay imposes character, setting, and prop constraints, then changes who knows the contents of a sealed envelope. Each task begins a fresh conversation; only its revision receives its own draft as conversation history. The essay deliberately tests reasoning from supplied material rather than factual recall.

Results go into a unique timestamped directory under `runs/` in your current working directory. Each task has readable Markdown outputs, exact prompts, full API responses, request settings, timings, mechanical checks, and a short human-review rubric. Settings and successful drafts remain saved if a later request fails. A failed draft skips its dependent revision and the runner continues to the next task, exiting nonzero if any request failed.

Word ranges and heading checks are indicators, not quality scores. Heading checks recognize ordinary Markdown headings but may miss unusual formatting. Read for causal reasoning, feasibility, continuity, substantive revision, and unnecessary repetition. A response with `done_reason` equal to `length` may have hit the token budget; increase `--tokens` before interpreting it as a writing failure. There is no automatic semantic or factual grader.

Keep temperature, token budget, context, and seed identical when comparing models. Repeat at seeds 42, 43, and 44 to check variability, for example `bash run.sh --model granite4.1:3b --seed 43`. A shared seed does not make different models produce equivalent random samples. Results also depend on installed model files, quantization, Ollama version, and hardware; record `ollama --version` and `ollama show MODEL` alongside comparisons if you want reproducibility. Timings include model loading and are not pure generation-speed benchmarks.

Use `--task essay` or `--task screenplay` to isolate a task, `--no-revision` for first drafts only, and `--temperature 0.7` to explore more variable writing. The defaults use temperature 0.3, seed 42, 2,500 output tokens, and an 8,192-token context. Edit TASKS in lab.py to add your own experiments. Judge the texts without model names visible where practical, and retain concrete examples of failures rather than trusting a single aggregate grade.

These experiments are intentionally short. Success here does not demonstrate the ability to sustain a whole book, full screenplay, or large software project. Next useful steps would be expanding an approved outline one section at a time and measuring whether constraints survive across sections.
