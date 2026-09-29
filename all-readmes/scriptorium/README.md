# Scriptorium

A durable, metadata-driven public catalogue for Flyxion works and executable Book Machines.

## Current public surfaces

- [Formatio idearum interlinearis](https://standardgalactic.github.io/scriptorium/formatio_idearum_interlinearis.pdf)
- [Formatio idearum per densas coertiones](https://standardgalactic.github.io/scriptorium/) — *Audio Overview*

## Catalogue infrastructure

Repository layout is data-first:

- `books/` — per-work metadata, covers, and publication artifacts
- `tools/` — per-tool metadata and optional static browser applications
- `collections/` — subject taxonomy
- `scripts/` — validation/build/catalogue tooling
- `site/` — static assets and templates
- `dist/` — generated website output
- `docs/publishing_model.md` — publishing workflow and schema
- `docs/work-edition-artifact-architecture.md` — Work ↔ Tool architecture with Work → Edition → Artifact publication structure

## Build and validate

From `/home/runner/work/scriptorium/scriptorium`:

```bash
python scripts/validate.py
python scripts/build.py
```

This generates a static catalogue where Library and Tools pages derive from metadata records rather than hand-coded pages.

## Discovery-first intake

Before manually adding new records under `books/`, run archaeology discovery from the profile README and repository corpus:

```bash
python scripts/discover.py
```

This generates review-ready candidate datasets in `/home/runner/work/scriptorium/scriptorium/discovery/output/` without publishing them.

## Publishing a New Work

From `/home/runner/work/scriptorium/scriptorium`:

```bash
python scripts/add-book.py /path/to/book --id book-slug
python scripts/validate.py
python scripts/build.py
```

After `add-book.py`, update the generated `books/<work-id>/book.json` and `books/<work-id>/description.md` as needed, then rerun validate/build.

## Adding a New Tool (Book Machine)

Create a metadata-driven tool folder:

```text
tools/
  <tool-id>/
    tool.json
    description.md
    app/                    # optional static browser app assets
```

Minimum `tool.json` fields:

- `id`
- `title`
- `type` (`simulator`, `explorer`, `calculator`, `visualizer`, `experiment`)
- `status` (`experimental`, `prototype`, `stable`, `archived`)
- `platform` (`web`, `desktop`, `cli`, `notebook`, `other`)
- `description`
- `topics` (non-empty list)
- `entrypoint` (absolute path under `/tools/<tool-id>/`)

Optional relationship/provenance fields:

- `related_works` (many-to-many links into `books/`)
- `inspired_by` (bibliographic/provenance records, not Scriptorium-owned Works)

Then run:

```bash
python scripts/validate.py
python scripts/build.py
```

Generated pages include `/tools/` and `/tools/<tool-id>/`.

![](scriptorium-infographic.png)
