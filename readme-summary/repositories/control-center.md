# control-center

**Summary**

The *control-center* repository provides a framework for **patch‑sync files**, which are optional, versioned artifacts that repositories can opt into via configuration or pull request (PR) labels. These files enable incremental adoption of new features without requiring full project rewrites.

- **Purpose**: To allow selective integration of experimental or advanced functionality across multiple projects.
- **Usage**:
  - Repositories list desired versions in their sync config (`sync.yml`) and apply appropriate PR labels.
  - Control‑center maintainers publish new files, version them using semantic versioning (vX.Y.Z), and document changes in the CHANGELOG.
- **Structure**: Files are organized by language or domain under `patch-sync/` directories (e.g., global, python, nodejs, go, terraform, rust) to support cross‑language compatibility.
- **Versioning**: Follows semantic versioning; each file’s front matter and filename must reflect the same version number. Detailed guidelines are in `docs/SYNC-FILE-VERSIONING.md`.
- **Examples**:
  - *Advanced CI Pipeline* (global/advanced-ci-v1.0.0.yml) adds multi‑stage builds, parallel testing, and advanced caching.
  - *Experimental Features* (global/experimental-feature-v0.1.0.yml) offers beta capabilities like mutation testing but is marked pre‑release with potential breaking changes.
  - *Python Testing Enhancements* (python/advanced-testing-v1.0.0.yml) introduces property‑based and performance benchmarks for Python projects.

**Relationships**: Patch‑sync files are complementary to the mandatory `always-sync` and `initial-only` directories, which contain essential configurations required by all repositories using control‑center.

**Status**: The system is actively maintained but considered experimental; new versions should be treated with caution due to possible breaking changes in pre‑release files.

**KEYWORDS**: patch sync files, versioned optional features, semantic versioning, GitHub sync config, experimental capabilities, cross‑language integration.
