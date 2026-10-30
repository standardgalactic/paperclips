# Paperclips

Paperclips is a repository documentation collection and analysis workspace. It gathers README files from repositories owned by a selected GitHub account, preserves their directory structure, and uses a locally running language model to produce repository summaries and broader syntheses.

The default account is `standardgalactic`. The purpose is to make a large collection of research, writing, software, and experimental projects easier to 
navigate, including projects whose documentation is nested below the repository root.

## How it works

The collection scripts use the GitHub API to enumerate repositories owned by the selected account, excluding repositories marked as forks. They download README files without cloning the repositories themselves.

The Python summarizer processes the collected documents through Ollama. It first summarizes individual documents, then 
combines those summaries into batches, and finally produces a global account of the collection. Its prompts ask the model to preserve project names, technical terminology, explicit relationships, and indications of incomplete work while avoiding unsupported connections.

This is document summarization through model inference. The supplied code does not implement model training or fine-tuning.

## Repository contents

`collect-readmes.sh` downloads 
the root README from each eligible repository.

`collect-nested-readmes.sh` searches repository trees for README files at any directory depth. It preserves their relative paths and skips existing nonempty destination files.

`summarize-readmes.py` generates individual summaries, batch syntheses, and a global synthesis using a local Ollama endpoint.

`all-readmes/` contains collected source documents. 
`readme-summary/` contains generated summaries and associated metadata.

## Requirements

Collection requires Bash, the GitHub CLI (`gh`), `jq`, and GitHub authentication with access to the repositories being queried. Summarization requires Python 3 and a running Ollama server. The Python script uses the standard library and requires no additional Python packages.

The default Ollama endpoint is `http://localhost:11434/api
/generate`, and the default model is `granite4.1:3b`.

## Collecting documentation

Authenticate the GitHub CLI if necessary:

```bash
gh auth login
```

Collect root READMEs using the default account and output directory:

```bash
bash collect-readmes.sh
```

Collect README files from all directory depths:

```bash
bash collect-nested-readmes.sh
```

Either collector accepts an account name and an output directory:

```bash
bash collect-readmes.sh ACCOUNT collected-readmes
bash collect-nested-readmes.sh ACCOUNT collected-readmes
```

The nested collector can supplement an existing collection, but it does not refresh files that already exist and contain data. Use a new output directory when a fresh snapshot is needed.

## Generating summaries

With Ollama running, obtain the default model:

```bash
ollama pull granite4.1:3b
```

Generate summaries using the 
default paths:

```bash
python3 summarize-readmes.py
```

Specify another input directory, output directory, model, or batch size:

```bash
python3 summarize-readmes.py collected-readmes \
  --output collected-summary \
  --model granite4.1:3b \
  --batch-chars 60000
```

The batch size is measured approximately in characters, rather than tokens. It limits the grouping of individual summaries for batch synthesis; it does not truncate an individual README.

The final synthesis is written to:

```text
readme-summary/GLOBAL_SUMMARY.md
```

Individual and batch summaries can be reused when their recorded source hashes and model names match. The global synthesis is 
regenerated on each completed run.

## Interpretation and limitations

Generated summaries are navigation aids. Claims about a project's implementation, results, or relationship to another project should be checked against its original documentation and code.

Collection is limited by GitHub access permissions, API availability, rate limits, and repository-tree responses. An absent document does not establish that a repository has no documentation.

The current summarizer names individual outputs by repository rather than by the full source-document path. When a repository contains multiple README files, their summaries can overwrite one another. Preserve the collected source documents and account for this limitation when interpreting a synthesis of nested documentation.

Collected documents retain their original authorship and applicable license terms.
