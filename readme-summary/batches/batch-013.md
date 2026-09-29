# Batch 13

**Flyxion Corpus Overview**

The Flyxion corpus is a curated collection of documents derived from TeX files—primarily LaTeX sources—that have been compiled using LuaLaTeX. Its purpose is to provide a machine‑readable environment for corpus analysis (e.g., word counts, duplicate detection) while preserving provenance information such as original PDFs and extracted text.

### Repository Structure

| Directory / Script | Purpose |
|--------------------|---------|
| **`flyxion-inventory.sh`** | Generates an inventory of root documents by scanning TeX files for `\documentclass`. |
| **`collect-flyxion-corpus.sh`** | Downloads PDFs and extracts text, placing artifacts under `build/` (intentionally untracked). |
| **`compile-flyxion-corpus.sh`** | Compiles each document twice; failures or timeouts are logged but do not abort subsequent builds. |
| **`extract-flyxion-text.sh`** | Uses `pdftotext` to produce plain‑text versions of PDFs for analysis. |
| **`analyze-flyxion-build.sh`** | Produces compilation manifests, duplicate reports, and a corpus‑level summary (e.g., total word count). |

### Build Pipeline

1. **Discovery** – The inventory script scans the repository for TeX files containing `\documentclass`, identifying potential root documents.
2. **Collection** – For each identified document:
   - Download the PDF version of the compiled output.
   - Run `pdftotext` to extract text.
3. **Compilation** – Each PDF is recompiled with LuaLaTeX twice (first pass for layout, second for final rendering). Errors or timeouts are recorded in logs without stopping further processing.
4. **Extraction & Analysis** – Text files are normalized and fed into analysis scripts that generate:
   - Word counts per document.
   - Duplicate detection across the corpus.
   - Manifests detailing compilation steps and artifacts.

### Technical Requirements

- **Environment**: Unix‑like system with Bash and GNU utilities installed.
- **Dependencies** (via `gh`):
  - `gh`: GitHub CLI for repository interactions.
  - `jq`: JSON processor for parsing build logs.
  - `perl`: Scripting capabilities for text manipulation.
  - `ripgrep`: Fast grep replacement for pattern searching in files.
  - `sha256sum`: Integrity verification of downloaded artifacts.
  - `flock`: File locking to prevent concurrent write conflicts during log generation.
  - `timeout`: Limits execution time for compilation steps that may hang.
  - `lualatex`: Core engine for LaTeX compilation (ensuring proper PDF output).
  - `pdfinfo` & `pdftotext`: Tools for extracting metadata and converting PDFs to plain text.

### Limitations & Considerations

- **Modular Documents**: Some TeX files may lack required dependencies (e.g., bibliography packages, external fonts), leading to compilation failures that signal missing resources rather than document quality issues.
- **GitHub Contributions**: The inventory script can be regenerated from recent GitHub activity using the provided scripts, allowing dynamic updates if new repositories are added or existing ones modified.

### Keywords

- **Flyxion corpus**, **TeX files**, **provenance preservation**, **LuaLaTeX compilation pipeline**, **corpus analysis**, **inventory script**, **GitHub contribution detection**.

This structured approach ensures that researchers can perform rigorous linguistic and textual analyses on the compiled documents while retaining traceability to their original TeX source files.
