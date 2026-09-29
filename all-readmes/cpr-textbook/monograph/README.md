# Constraint, Projection, and Reachability
## A Geometric Theory of Cognition, Meaning, and Complex Systems

**Author:** Flyxion  
**Engine:** LuaLaTeX  
**Status:** Active development

---

## Directory Structure

```
cpr-textbook/
├── main.tex                   ← Root driver (includes all parts)
├── Makefile
├── .latexmkrc
├── scripts/
│   └── generate_stubs.py      ← Creates empty chapter stubs
├── assets/
│   ├── bib/
│   │   └── cpr.bib            ← Master bibliography
│   ├── figures/               ← Raster images (.pdf, .png, .jpg)
│   └── tikz/
│       ├── macros.tex         ← All CPR notation (\Adm, \Reach, \rsvp …)
│       ├── thmstyles.tex      ← Theorem / definition box environments
│       ├── headerstyles.tex   ← titlesec chapter/section styling
│       ├── pagestyle.tex      ← fancyhdr headers and footers
│       ├── tocstyle.tex       ← titletoc configuration
│       ├── lststyles.tex      ← listings + Lean4 language definition
│       ├── crefnames.tex      ← cleveref label names
│       └── indexstyle.ist     ← makeindex style
├── front/
│   ├── titlepage.tex
│   ├── copyright.tex
│   ├── dedication.tex         ← stub
│   ├── epigraphs.tex          ← stub
│   ├── preface.tex
│   ├── acknowledgements.tex   ← stub
│   └── notation.tex
├── parts/
│   ├── 01-constraint/         ← Part I (6 chapters) — fully drafted
│   ├── 02-foundations/        ← Part II (9 chapters) — stubs
│   ├── 03-admissibility/      ← Part III
│   ├── 04-compression/        ← Part IV
│   ├── 05-cognition/          ← Part V
│   ├── 06-language/           ← Part VI
│   ├── 07-computation/        ← Part VII
│   ├── 08-biological/         ← Part VIII
│   ├── 09-institutions/       ← Part IX
│   ├── 10-physics/            ← Part X (RSVP lives here)
│   ├── 11-ai/                 ← Part XI
│   └── 12-unification/        ← Part XII
└── back/
    ├── appendix-a-rsvp-formal.tex
    ├── appendix-b-hydra-categorical.tex
    ├── appendix-c-clio-mem8.tex
    ├── appendix-d-spherepop.tex
    ├── appendix-e-notation-index.tex
    └── colophon.tex
```

---

## Building

### Prerequisites

```bash
# Ubuntu / Debian
sudo apt install texlive-full latexmk python3

# Or TeX Live manually (recommended for latest packages)
# https://www.tug.org/texlive/
```

Required fonts: **TeX Gyre Pagella** and **TeX Gyre Pagella Math**
(both included in `texlive-full`).

### Commands

```bash
make pdf          # Full build (LuaLaTeX × 3 + biber + makeindex)
make fast         # Single-pass, no bibliography
make draft        # Draft mode (no microtype, faster)
make watch        # Continuous rebuild on save (requires evince or similar)
make count        # Approximate word count across all .tex files
make countbypart  # Word count broken down by part
make stubs        # Regenerate stub files for any missing chapters
make clean        # Remove auxiliary files
make distclean    # Remove all build artefacts including PDF
```

### Manual build (if latexmk is not available)

```bash
mkdir -p build
lualatex -output-directory=build main.tex
biber build/main
lualatex -output-directory=build main.tex
makeindex -s assets/tikz/indexstyle.ist build/main.idx
lualatex -output-directory=build main.tex
```

---

## Key Macros

See `assets/tikz/macros.tex` for the full list. Important ones:

| Macro | Output |
|---|---|
| `\CPRtriad` | Constraint → Projection → Reachability |
| `\Adm` | Admissibility manifold $\mathcal{A}$ |
| `\admset{x}` | Admissible futures $\mathcal{A}(x)$ |
| `\rsvp` | RSVP triple $(\Phi, \mathbf{v}, S)$ |
| `\colimAdm` | Collective admissibility colimit |
| `\HYDRA`, `\CLIO`, `\RSVP` | Framework name small-caps |
| `\keyterm{word}` | Bold + index entry |
| `\mnote{text}` | Margin note |

## Environments

```latex
\begin{theorem}[Name]...\end{theorem}
\begin{definition}[Name]...\end{definition}
\begin{proposition}...\end{proposition}
\begin{lemma}...\end{lemma}
\begin{corollary}...\end{corollary}
\begin{example}...\end{example}
\begin{remark}...\end{remark}
\begin{conjecture}...\end{conjecture}
\begin{openproblem}...\end{openproblem}
\begin{insight}[Title]...\end{insight}    % gold-ruled key insight box
\begin{cprtriad}...\end{cprtriad}         % centred CPR triad display
```

---

## Workflow Notes

- Each chapter is a separate `\include`d file.  
  Write one chapter at a time; the build still works.
- Bibliography: add entries to `assets/bib/cpr.bib` in BibLaTeX format.  
  Cite with `\parencite{key}` (parenthetical) or `\textcite{key}` (inline).
- Index: use `\keyterm{word}` for the first definition of a term.  
  Manual entries: `\index{word}` or `\index{word!subentry}`.
- Figures: place PDFs/PNGs in `assets/figures/` and include with  
  `\includegraphics[width=\linewidth]{figures/myfile}`.
- TikZ diagrams: either inline in the chapter file or as  
  `\input{assets/tikz/mydiagram}` for reusable diagrams.

---

## Chapter Template

Every new chapter should open with:

```latex
\chapter{Title}
\label{ch:label}

\epigraph{Quote}{Source}

\noindent
Opening paragraph...
```

End with `\section*{Exercises}` and a numbered exercise list.

---

## The CPR Triad

Every chapter should ultimately connect its local content
back to:

$$\text{Constraint} \;\longrightarrow\; \text{Projection} \;\longrightarrow\; \text{Reachability}$$

Use `\begin{cprtriad}...\end{cprtriad}` to display it prominently
at key moments.
