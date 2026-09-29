# flyxion-corpus

**Summary**

The *flyxion-corpus* repository aggregates all TeX files attributed to Flyxion that appear across various GitHub repositories (originally discovered in `standardgalactic`). It preserves the full provenance of each file—storing the original owner, repository name, and internal path under a normalized hierarchy (`sources/OWNER/REPOSITORY/original/path/document.tex`). The corpus contains 965 out‑of‑967 candidate TeX files identified by an inventory script; inclusion does not imply completeness or endorsement.

The primary purposes are:

1. **Snapshot preservation** – keeping a recoverable copy of the distributed sources.
2. **Provenance tracking** – retaining metadata that links each file back to its original repository and path.
3. **Compilation pipeline** – providing repeatable LuaLaTeX builds for all collected documents, even if they require additional packages or fonts not present in this corpus.
4. **Analysis readiness** – generating readable UTF‑8 text from PDFs and producing machine‑readable manifests (e.g., compilation outcomes, word counts, duplicate groups) to enable corpus analysis.

The repository structure separates scripts for discovery (`flyxion-inventory.sh`), collection (`collect-flyxion-corpus.sh`), compilation (`compile-flyxion-corpus.sh`), extraction (`extract-flyxion-text.sh`), and analysis (`analyze-flyxion-build.sh`). Generated artifacts (PDFs, text files, logs) are placed under `build/`, which is intentionally left untracked.

**Requirements**: Unix‑like environment with Bash plus GNU utilities; external commands include `gh`, `jq`, `perl`, `ripgrep`, `sha256sum`, `flock`, `timeout`, `lualatex`, `pdfinfo`, and `pdftotext`.

The build script runs the full pipeline, discovering root documents via `\documentclass` in TeX files. Each root is compiled twice; failures or timeouts are logged without aborting subsequent builds. Output mirrors source paths under `build/`, providing PDFs, extracted text, logs, compilation manifests, duplicate reports, and a corpus‑level summary.

To regenerate the inventory from GitHub contributions, run the provided scripts to rebuild the list of repositories and collect missing files if needed. Compilation limitations note that some modular documents may lack required dependencies (chapters, bibliographies, fonts), so build failures often signal missing resources rather than document quality issues.

**KEYWORDS**: Flyxion corpus, TeX files, provenance preservation, LuaLaTeX compilation pipeline, corpus analysis, inventory script, GitHub contribution detection.
