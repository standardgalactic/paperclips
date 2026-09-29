# Batch 19

**playfloor**

**Summary**

The *playfloor* repository is a LuaLaTeX‑based textbook template designed for creating scholarly documents that emphasize semantic infrastructure and formal notation. It provides:

- A **master document (`main.tex`)** with built‑in build automation via `build.sh`.
- Extensive **box environments** (definition, theorem, example, warning, etc.) for structured presentation.
- Custom **notation commands** (`\rsvp`, `\sphere`, `\eval`, …) that render specific symbols and triples used throughout the text.
- A directory layout separating source chapters, bibliography handling with `biblatex`/`biber`, indexing, and 3D diagrams using `tikz‑3dplot`.
- Build instructions (single‑run, clean, watch modes) and manual compilation steps for flexibility.

The template is intended for academic work that requires precise typographic control, rich mathematical notation, and modular chapter organization. It relies on TeX Live 2023+ or MiKTeX 23+, with a curated set of packages (`fontspec`, `unicode-math`, `tcolorbox`, etc.) to support the required features.

**KEYWORDS:** LuaLaTeX, textbook template, semantic infrastructure, formal notation, box environments, custom commands, 3D diagrams, TeX Live, BibLaTeX.
