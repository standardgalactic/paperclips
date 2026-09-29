# bash-functions

> Version: 0.1.0

Data and pipelines associated with papers from the lab.

## Granite essay pipeline subsystem

A modular, compiler-like essay generation pipeline with Ollama Granite models. Each pipeline stage is independent, validates inputs, and produces reproducible intermediate artifacts.

## Computational laboratories

- [`labs/radiative-switch/`](labs/radiative-switch/) — Reproducible radiative-switch computation lab with staged experiment modules plus companion notebooks for exploration and design.
- [`labs/magnetic-fluidic-mathematics/`](labs/magnetic-fluidic-mathematics/) — Formal magnetic-fluidic computing mathematics notes organized for simulation-oriented modeling workflows.
- [`labs/flash-reluctance-laboratory/`](labs/flash-reluctance-laboratory/) — Flash-reluctance hybrid-system laboratory notes covering state-space, dynamics, control, and optimization progression.

### Laboratory notebook policy

- Notebook execution is **intentional** and separate from shell `build`/`test`.
- Required notebooks:
  - `labs/flash-reluctance-laboratory/flash_reluctance_laboratory.ipynb`
  - `labs/magnetic-fluidic-mathematics/magnetic_fluidic_computing_lab.ipynb`
  - `labs/radiative-switch/radiative-switch-laboratory.ipynb`
- Optional notebook:
  - `labs/radiative-switch/radiative-switch-design-studio.ipynb` (interactive; requires `ipywidgets`)
- Standard execution commands:
  - `scripts/manage.sh notebooks required` (default policy set)
  - `scripts/manage.sh notebooks all` (includes optional notebooks)
  - `scripts/manage.sh workflow validate` (validate labs manifest, project READMEs, and notebook paths)
  - `scripts/manage.sh workflow notebooks <project-id> [required|all]` (run notebook workflow for a single lab project)
- Execution is CI-safe: notebooks run via `nbconvert` into a temporary output directory and source notebooks are not modified.
- Notebook workflow metadata is centralized in `labs/projects.manifest`.

### Design highlights

- **Single-responsibility modules** under `lib/` with clear dependencies
- **Composable orchestration** via `scripts/granite-pipeline.sh`
- **Explicit validation** of inputs, environment, and intermediate outputs
- **Timestamped logging** with optional JSON mode (`BF_LOG_JSON=1`)
- **Stage metadata tracing** in `.trace/meta/*.json` for debugging and reproducibility
- **Multi-model workflow**:
  - `granite4.1:3b` for fast, iterative drafting
  - `granite4.1:8b` for outline, review, revision, and final editorial control
- **PDF compilation** support via Pandoc and LaTeX (optional)

### Repository layout

```
bash-functions/
├── lib/
│   ├── context.sh        Context assembly from brief, instructions, notes, memory
│   ├── errors.sh         Error handling and stack traces
│   ├── filesystem.sh     File system utilities (paths, validation, cleanup)
│   ├── logging.sh        Structured logging (text and JSON modes)
│   ├── markdown.sh       Markdown utilities (word count, validation)
│   ├── ollama.sh         Ollama model interaction and validation
│   ├── pandoc.sh         Pandoc conversions (Markdown → LaTeX → PDF)
│   ├── prompts.sh        Pipeline stage prompts (outline, draft, review, revision, final)
│   ├── tracing.sh        Execution tracing and metadata recording
│   └── validation.sh     Input validation and environment checks
├── scripts/
│   ├── manage.sh         Repository management (clean, build, test, version, release)
│   ├── granite-pipeline.sh  Main essay pipeline orchestrator
│   ├── retrieve-memory.sh   Optional memory retrieval helper
│   ├── init-project.sh      Project scaffold generator for new essay runs
│   └── doctor.sh            Environment dependency checker
└── tests/
    └── granite_modules_test.sh  Unit tests for lib modules
```

## How it works

The Granite pipeline reads a project brief and optional context files, then orchestrates multiple model stages:

1. **Context Assembly**: Merges brief, instructions, source notes, and retrieved memory
2. **Outline Generation**: Stronger model produces structure from context
3. **Draft Creation**: Faster model drafts content following outline
4. **Review Phase**: Stronger model reviews draft quality and completeness
5. **Revision**: Stronger model applies review feedback
6. **Final Editorial**: Stronger model polishes and finalizes
7. **Export**: Converts final Markdown to LaTeX and optionally to PDF

All intermediate outputs and prompts are saved for inspection and reproducibility.

## Quick start

### Prerequisites

- **Bash 4.0+**
- **Ollama** with Granite models: `ollama pull granite4.1:3b granite4.1:8b`
- **Pandoc** (for format conversion)
- **Python 3** (for Markdown validation)
- **LaTeX** (optional, for PDF output): `lualatex` or `pdflatex`
- **ShellCheck** (optional, for linting)

### Setup and verify tooling

```bash
git clone https://github.com/standardgalactic/bash-functions.git
cd bash-functions
chmod +x scripts/*.sh

# Validate shell scripts + tests
scripts/manage.sh build

# Verify required runtime dependencies
scripts/doctor.sh
```

### Running the pipeline

```bash
# Create a project directory with the required brief
mkdir my-project
cat > my-project/brief.md << 'EOF'
# My Paper Brief
This is my research topic...
EOF

# Run the managed pipeline
scripts/manage.sh run ./my-project

# Output is in my-project/build/
# - context.md, outline.md, draft.md, review.md, revised.md, final.md
# - final.pdf (if COMPILE_PDF=1, default)
# Tracing data in my-project/.trace/
```

### Project input structure

```
my-project/
├── brief.md              Required: project brief/topic description
├── instructions.md       Optional: project-specific constraints/requirements
├── source-notes.md       Optional: reference materials to consider
└── memory.md             Optional: pre-retrieved context/memory (or generate with retrieve-memory.sh)
```

## Management commands

### Using `scripts/manage.sh`

| Command | Description |
|---------|-------------|
| `scripts/manage.sh clean` | Remove build artifacts (`build/`), trace directories (`.trace/`), and log files |
| `scripts/manage.sh lint` | Run ShellCheck against `lib/*.sh` and `scripts/*.sh` |
| `scripts/manage.sh test` | Run `tests/granite_modules_test.sh` |
| `scripts/manage.sh build` | Run `lint` then `test` |
| `scripts/manage.sh notebooks [required\|all\|list]` | Run laboratory notebooks via `jupyter nbconvert` (separate from `build`) |
| `scripts/manage.sh workflow list` | Show all lab projects and notebook mappings from `labs/projects.manifest` |
| `scripts/manage.sh workflow validate` | Validate lab workflow metadata, project README presence, and notebook files |
| `scripts/manage.sh workflow notebooks <project-id> [required\|all]` | Execute notebook workflow for one laboratory project |
| `scripts/manage.sh run <project>` | Execute the Granite pipeline for a project directory |
| `scripts/manage.sh version show` | Print current version from `VERSION` |
| `scripts/manage.sh version bump [major|minor|patch]` | Bump semantic version (default: `patch`) and sync README version line |
| `scripts/manage.sh version set <version>` | Set an explicit version and sync README version line |
| `scripts/manage.sh release [major|minor|patch]` | Run `build`, bump version, and update release-related docs (`VERSION`, README version line) |

### Command examples

```bash
# Show version
scripts/manage.sh version show

# Bump version (patch, minor, major)
scripts/manage.sh version bump minor

# Set a specific version
scripts/manage.sh version set 0.1.0

# Build and test
scripts/manage.sh build

# Run required laboratory notebooks
scripts/manage.sh notebooks required

# Show cross-project workflow map
scripts/manage.sh workflow list

# Validate manifest-backed workflow metadata
scripts/manage.sh workflow validate

# Run notebooks for a single project
scripts/manage.sh workflow notebooks radiative-switch all

# Run linter only
scripts/manage.sh lint

# Run test suite
scripts/manage.sh test

# Clean artifacts
scripts/manage.sh clean

# Prepare a release
scripts/manage.sh release minor

# Run pipeline on a project
scripts/manage.sh run ./my-project
```

### Additional utility scripts

| Script | Description |
|--------|-------------|
| `scripts/init-project.sh <project>` | Create a new project scaffold with `brief.md`, `instructions.md`, `source-notes.md`, and `memory.md` |
| `scripts/init-project.sh <project> --force` | Recreate scaffold files and overwrite existing content |
| `scripts/doctor.sh` | Check required (`bash`, `python3`, `ollama`, `pandoc`) and optional tooling availability |

## Environment variables

| Variable | Default | Category | Description |
|----------|---------|----------|-------------|
| `DRAFT_MODEL` | `granite4.1:3b` | Pipeline | Ollama model for drafting stage |
| `REVIEW_MODEL` | `granite4.1:8b` | Pipeline | Ollama model for review and revision stages |
| `FINAL_MODEL` | `granite4.1:8b` | Pipeline | Ollama model for final editorial stage |
| `OLLAMA_NUM_CTX` | `32768` | Pipeline | Ollama context window size (tokens) |
| `COMPILE_PDF` | `1` | Pipeline | Compile PDF output (`0` disables PDF compilation) |
| `TRACE` | `1` | Pipeline | Enable execution tracing to `.trace/` |
| `BF_LOG_LEVEL` | `INFO` | Logging | Log level: `DEBUG`, `INFO`, `WARN`, `ERROR` |
| `BF_LOG_JSON` | `0` | Logging | Emit JSON logs when set to `1` |
| `BF_NOTEBOOK_KEEP_OUTPUT` | `0` | Notebooks | Keep executed notebook artifacts instead of deleting temp outputs (`1` keeps files) |
| `BF_LOG_FILE` | (unset) | Logging | Log file path (set internally by pipeline) |
| `OLLAMA` | `ollama` | Tool path | Path to Ollama executable |
| `PYTHON` | `python3` | Tool path | Path to Python executable used for validation |
| `PANDOC` | `pandoc` | Tool path | Path to Pandoc executable |
| `LATEX_ENGINE` | `lualatex` | Tool path | LaTeX engine (`lualatex` or `pdflatex`) |

### Examples

```bash
# Use debug logging and save to file
BF_LOG_LEVEL=DEBUG BF_LOG_JSON=0 scripts/manage.sh run ./my-project

# Use JSON logging, skip PDF, use smaller context
BF_LOG_JSON=1 COMPILE_PDF=0 OLLAMA_NUM_CTX=16384 scripts/manage.sh run ./my-project

# Use custom models
DRAFT_MODEL=neural-chat:latest REVIEW_MODEL=mistral:latest scripts/manage.sh run ./my-project

# Keep executed notebook outputs for inspection
BF_NOTEBOOK_KEEP_OUTPUT=1 scripts/manage.sh notebooks required
```

## Testing

```bash
# Run test suite
scripts/manage.sh test

# Or run directly
tests/granite_modules_test.sh
```

## Module documentation

### `lib/context.sh`
Assembles multi-part project context from brief, instructions, source notes, and memory.

### `lib/errors.sh`
Error handling, timestamps, and stack traces for debugging pipeline failures.

### `lib/logging.sh`
Structured logging with configurable levels (DEBUG, INFO, WARN, ERROR) and optional JSON output.

### `lib/validation.sh`
Input validation: file existence, program availability, Ollama model availability.

### `lib/filesystem.sh`
File system operations: directory creation, path resolution, cleanup.

### `lib/tracing.sh`
Execution metadata recording for reproducibility and auditing.

### `lib/prompts.sh`
System prompts for each pipeline stage (outline, draft, review, revision, final).

### `lib/ollama.sh`
Ollama API interaction: model validation, inference calls with streaming.

### `lib/pandoc.sh`
Document format conversion: Markdown → LaTeX → PDF.

### `lib/markdown.sh`
Markdown utilities: word count, format validation.

## Contributing

All shell scripts follow:
- **ShellCheck** linting standards
- **Bash 4.0+** compatibility
- **Single-responsibility principle** for functions
- **Documented arguments and return codes** for all exported functions

Before committing:
```bash
# Equivalent pre-commit checks (lint + tests)
scripts/manage.sh build

# Or run checks independently
scripts/manage.sh lint
scripts/manage.sh test
```

## License

See LICENSE file (if present).

## Support

For issues, questions, or contributions, open an issue or pull request on GitHub.
