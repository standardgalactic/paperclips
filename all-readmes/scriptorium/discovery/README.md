# Discovery and Curation

This directory supports discovery-first portfolio intake.

## Separation of concerns

```text
GitHub corpus
  -> discovery
  -> candidates
  -> review
  -> catalogue
```

Discovery output is advisory only. Nothing under `discovery/output/` is auto-imported into `books/`.

## Review decisions

Use `/home/runner/work/scriptorium/scriptorium/discovery/review-decisions.json` to store manual curation decisions keyed by:

`<seed_key>|<repository>|<path>`

Example:

```json
{
  "the-calculus-of-commitment|standardgalactic/research-projects|paper/calculus-of-commitment.tex": {
    "status": "accepted",
    "notes": "Canonical manuscript source.",
    "updated_by": "@standardgalactic"
  }
}
```

Valid statuses are:

- `pending`
- `accepted`
- `rejected`
- `needs-review`

## Running discovery

From `/home/runner/work/scriptorium/scriptorium`:

```bash
python scripts/discover.py
```

Optional controls:

```bash
python scripts/discover.py --repo-limit 20 --seed-limit 60 --tex-limit 200
```

For higher GitHub API limits:

```bash
GITHUB_TOKEN=ghp_xxx python scripts/discover.py
```

Outputs are written to `/home/runner/work/scriptorium/scriptorium/discovery/output/`.
