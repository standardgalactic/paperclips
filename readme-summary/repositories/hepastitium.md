# hepastitium

**Summary**

Hepastitium is not a single software package but a research repository that houses source material, experimental utilities, and the LaTeX source for *A Relativistic Theory of Longevity*. The primary content is a monograph written in LaTeX; building it requires installing a TeX Live environment on Debian/Ubuntu systems and running two `pdflatex` passes to resolve cross‑references. Optional scripts include:

- **extract-text.py**: A Python utility (requiring Beautiful Soup and PyMuPDF) that extracts text from PDF/MHTML files placed in the current directory.
- **get-chunksize.sh** & **get-summaries.sh**: Tools for proposing chunk sizes of text files and generating summaries using a local Ollama model (`vanilj/phi-4`). These scripts are experimental language experiments rather than core components.

The repository is incomplete; it contains only the monograph source and selected utilities, with no full build or deployment instructions beyond those provided. KEYWORDS: Hepastitium, LaTeX, Relativistic Theory of Longevity, text extraction, Ollama model, Python utility.
