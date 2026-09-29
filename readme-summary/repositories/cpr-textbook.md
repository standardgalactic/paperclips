# cpr-textbook

**Summary**

The *cpr-textbook* repository is an active development project authored by Flyxion that presents a **geometric theory of cognition, meaning, and complex systems**. It organizes content into parts (e.g., Constraint → Projection → Reachability) using LuaLaTeX with LaTeX‑Gyre fonts for typesetting. The core concepts include:

- **Constraint**, **Projection**, and **Reachability** as the central triad.
- Notation macros such as `\Adm` (admissibility manifold), `\rsvp` (RSVP triple), and `\HYDRA`, `\CLIO`, `\RSVP` framework names.
- Environments for theorem, definition, proposition, lemma, corollary, example, remark, conjecture, open problem, and a special “insight” box.
- Workflow guidelines: chapters are separate `.tex` files included via `\include`; bibliography entries go into `assets/bib/cpr.bib`; indexing uses `\keyterm`.
- Visual elements like figures (PDF/PNG) placed in `assets/figures/`, TikZ diagrams stored in `assets/tikz/`, and margin notes with `\mnote`.

The README emphasizes building the document via a Makefile (`make pdf` for full build, etc.), maintaining a consistent macro set, and linking every chapter back to the **CPR triad** through highlighted displays.

**KEYWORDS:** constraint theory, projection geometry, reachability analysis, geometric cognition, complex systems modeling, LuaLaTeX documentation.
