# scriptorium

Summary:

The **scriptorium** repository is a tool designed for the discovery and curation of research materials within a GitHub corpus. It separates concerns into distinct directories: `discovery`, `candidates`, `review`, and `catalogue`. The discovery process generates advisory output that does not auto-import items into the `books/` directory, emphasizing manual review.

Review decisions are stored in `/home/runner/work/scriptorium/scriptorium/discovery/review-decisions.json`, using keys formatted as `<seed_key>|<repository>|<path>`. Valid statuses for these entries include `pending`, `accepted`, `rejected`, and `needs-review`.

To run the discovery process, execute `python scripts/discover.py` from the repository root. Optional parameters allow limiting the number of repositories (`--repo-limit`), seeds (`--seed-limit`), or LaTeX files (`--tex-limit`). For higher GitHub API rate limits, provide a personal access token via `GITHUB_TOKEN=ghp_xxx`.

Outputs are saved to `/home/runner/work/scriptorium/scriptorium/discovery/output/`, facilitating structured curation without automatic integration.

KEYWORDS:
scriptorium repository
discovery-first portfolio intake
GitHub corpus organization
review-decisions JSON storage
manual curation decisions
advisory output only
