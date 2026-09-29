# cutaway-reader

**Summary**

Cutaway Reader is an experimental spatial‑reading tool for collections of LaTeX documents (essays, books, etc.). It treats each work as a “level” with sections as chambers, subsections as alcoves, cross‑references (`\ref`) as two‑way tunnels, appendices as shafts. Works are organized in a galaxy where connections are defined by explicit citations and series order.

Two core principles guide its design:

1. **Meaning is recomputed; place is remembered** – Every `*.graph.json` file (the level graph) is rebuilt from the source files each time, while every `*.ledger.json` (placement ledger) is append‑only: once a chamber or work is placed it never moves.
2. **Nothing is inferred silently** – Proposed editions appear marked *proposed*, guessed lanes are labeled *suggestion* until an author declares them, and conflicting placements remain unresolved as *conflict*.

The repository provides command‑line utilities (`corpus.py`, `mine.py`, etc.) to:

- Import LaTeX sources (including multi‑file or zip archives) into per‑work graphs/ledgers.
- Build a full corpus graph and ledger, resolve edition choices, declare explicit lanes/suggestions/series.
- Generate reports of unresolved decisions, export the model for static HTML viewers, and run a suite of automated tests covering level semantics, incremental builds, schema validation, and viewer behavior.

Key files include:

- `corpus.py` – orchestrates multi‑work processing (add sources, build corpus, report conflicts).
- `mine.py` – processes individual LaTeX files into per‑work graphs/ledgers.
- `model.js` – defines the shared model for all interfaces (levels, reader log, portals, views).
- `build_viewer.py` – creates a static HTML site with interactive viewer (`cutaway-tty.js`) and documentation assets.

The project is accompanied by extensive documentation files (`SPEC.md`, `FORMATS.md`, etc.) that detail its design, file formats, and usage conventions. Tests cover every model component via Python‑based suites ensuring idempotence, correctness of placement ledgers, and proper handling of suggested lanes.

**KEYWORDS:** Cutaway Reader, spatial reading, LaTeX corpus, graph JSON, ledger JSON, edition proposal, lane suggestion, conflict resolution, interactive viewer, terminal client, automated testing.
