# Epicormic-Growth

**Summary**

Epicormic-Growth is an experimental software project that models biological growth using Git as its historical ledger. It starts with a single dormant trunk record and, via the provided Python script, generates up to 10,000 immutable commits (shoots). Each commit appends exactly one shoot to a canonical JSON Lines file (`growth/shoots.jsonl`), which stores each line’s SHA‑256 hash along with the previous record’s hash for integrity. Two derived views—`growth/organism.json` and `growth/organism.svg`—are deterministic projections of the complete organism from this ledger.

The script is safe by default; running it without the `--execute` flag validates the repository, calculates remaining work, and previews upcoming shoots before exiting. To actually commit locally and push every 250 commits (or all at once if resuming), use:

```bash
python3 epicormic_growth.py --execute --target 10000 --push-every 250
```

or

```bash
python3 epicormic_growth.py --execute --target 10000
git push
```

Resumption is supported; the script will continue from the last verified ledger record and refuses to run under dirty conditions or with an altered hash chain. The repository contains no dates or randomness—identical seed and shoot numbers always produce identical parent, angle, length, and color.

**KEYWORDS:** Epicormic Growth, Git history, biological growth model, JSON Lines ledger, deterministic commits, shoot generation, Python standard library, integrity hashes (SHA-256), organism projections (JSON & SVG).
