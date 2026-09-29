#!/usr/bin/env python3

import argparse
import hashlib
import json
import os
import re
import time
import urllib.request
from pathlib import Path

DEFAULT_MODEL = "granite4.1:3b"
OLLAMA_URL = "http://localhost:11434/api/generate"

INDIVIDUAL_PROMPT = """\
You are analyzing the README of one software, research, writing, or experimental
repository belonging to a much larger body of work.

Repository: {repo}

Produce a compact but information-dense summary.

Preserve:
- the repository's actual purpose;
- important concepts, theories, systems, experiments, software, or artifacts;
- distinctive terminology;
- mathematical or technical frameworks when present;
- relationships explicitly stated with other projects;
- implementation status, maturity, or incompleteness when the README makes it clear;
- particularly unusual or important claims.

Do not invent relationships or infer facts that are not supported by the README.
Do not write generic praise.
Do not spend space describing README formatting.

End with a line beginning:

KEYWORDS:

followed by 5-15 useful retrieval terms.

README:

{content}
"""

BATCH_PROMPT = """\
You are synthesizing summaries of repositories from a single research and
development corpus.

Produce a structured synthesis of the material below.

Identify:
- recurring research programs and conceptual families;
- software and engineering families;
- mathematical or scientific frameworks;
- recurring terminology;
- repositories that appear closely related;
- duplicated or substantially overlapping projects;
- important outliers;
- apparent progression from earlier ideas into later or more developed systems;
- unresolved questions or unfinished programs explicitly visible in the summaries.

Preserve repository names whenever making connections. Do not invent
relationships merely because two projects use vaguely similar language.

SOURCE SUMMARIES:

{content}
"""

GLOBAL_PROMPT = """\
You are constructing a global intellectual and technical map of a large corpus
of repositories. The input consists of batch syntheses ultimately derived from
repository READMEs.

Write a detailed global synthesis.

The result should explain:

1. The major research programs represented in the corpus.
2. The major software and engineering programs.
3. The principal mathematical, scientific, philosophical, and computational
   frameworks.
4. Concepts and terminology that recur across otherwise different repositories.
5. Important repository families and how their members differ.
6. Cases where an idea appears to migrate from one domain into another.
7. Repositories or ideas that are unusual outliers.
8. Areas with substantial duplication or multiple implementations.
9. Apparent historical or conceptual development, but only where supported by
   the supplied material.
10. Open, unfinished, or weakly developed directions visible in the corpus.
11. A repository index grouped by conceptual family.
12. A concise final account of what distinguishes this corpus as a whole.

Repository names are important evidence. Cite repository names throughout the
synthesis rather than dissolving everything into anonymous themes.

Do not introduce outside knowledge.
Do not assume that repeated terminology proves theoretical identity.
Distinguish explicit relationships from relationships inferred from similarity.

BATCH SYNTHESES:

{content}
"""

def ollama_generate(model, prompt, timeout=1800):
    payload = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": True,
        "options": {
            "temperature": 0.2,
        },
    }).encode("utf-8")

    request = urllib.request.Request(
        OLLAMA_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    chunks = []

    with urllib.request.urlopen(request, timeout=timeout) as response:
        for raw_line in response:
            if not raw_line.strip():
                continue

            event = json.loads(raw_line.decode("utf-8"))
            chunk = event.get("response", "")

            if chunk:
                # Tee Granite's output live to the terminal.
                print(chunk, end="", flush=True)
                chunks.append(chunk)

    print()
    print()

    return "".join(chunks).strip()

def safe_name(name):
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("_")


def file_hash(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(1024 * 1024):
            h.update(chunk)
    return h.hexdigest()


def read_text(path):
    return path.read_text(encoding="utf-8", errors="replace")


def find_readmes(root):
    readmes = []

    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue

        # The collector normally names files after repositories, but accept
        # common text/Markdown/reStructuredText extensions.
        if path.suffix.lower() not in {
            ".md", ".markdown", ".txt", ".rst", ".adoc", ""
        }:
            continue

        readmes.append(path)

    return readmes


def repository_name(root, path):
    rel = path.relative_to(root)

    # If the collector stores one directory per repository:
    if len(rel.parts) > 1:
        return rel.parts[0]

    # If files are flattened as repo.md, repo.rst, etc.
    return path.stem


def summarize_individual(root, path, outdir, model):
    repo = repository_name(root, path)
    digest = file_hash(path)

    basename = safe_name(repo)
    summary_path = outdir / "repositories" / f"{basename}.md"
    metadata_path = outdir / "repositories" / f"{basename}.json"

    if summary_path.exists() and metadata_path.exists():
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))

            if (
                metadata.get("sha256") == digest
                and metadata.get("model") == model
            ):
                print(f"SKIP {repo}")
                return repo, summary_path
        except Exception:
            pass

    content = read_text(path)

    prompt = INDIVIDUAL_PROMPT.format(
        repo=repo,
        content=content,
    )

    print(f"SUMMARIZE {repo}")

    summary = ollama_generate(model, prompt)

    summary_path.parent.mkdir(parents=True, exist_ok=True)

    summary_path.write_text(
        f"# {repo}\n\n{summary}\n",
        encoding="utf-8",
    )

    metadata_path.write_text(
        json.dumps(
            {
                "repository": repo,
                "source": str(path),
                "sha256": digest,
                "model": model,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    return repo, summary_path


def make_batches(items, max_chars):
    batches = []
    current = []
    current_size = 0

    for repo, text in items:
        block = f"\n\n===== REPOSITORY: {repo} =====\n\n{text}"

        if current and current_size + len(block) > max_chars:
            batches.append(current)
            current = []
            current_size = 0

        current.append((repo, text))
        current_size += len(block)

    if current:
        batches.append(current)

    return batches


def synthesize_batches(repository_summaries, outdir, model, max_chars):
    batches = make_batches(repository_summaries, max_chars)
    results = []

    batch_dir = outdir / "batches"
    batch_dir.mkdir(parents=True, exist_ok=True)

    for i, batch in enumerate(batches, start=1):
        path = batch_dir / f"batch-{i:03d}.md"

        content = "\n\n".join(
            f"===== {repo} =====\n{text}"
            for repo, text in batch
        )

        digest = hashlib.sha256(
            content.encode("utf-8")
        ).hexdigest()

        metadata_path = batch_dir / f"batch-{i:03d}.json"

        if path.exists() and metadata_path.exists():
            try:
                metadata = json.loads(
                    metadata_path.read_text(encoding="utf-8")
                )

                if (
                    metadata.get("sha256") == digest
                    and metadata.get("model") == model
                ):
                    print(f"SKIP batch {i}/{len(batches)}")
                    results.append(read_text(path))
                    continue
            except Exception:
                pass

        print(
            f"SYNTHESIZE batch {i}/{len(batches)} "
            f"({len(batch)} repositories)"
        )

        result = ollama_generate(
            model,
            BATCH_PROMPT.format(content=content),
        )

        path.write_text(
            f"# Batch {i}\n\n{result}\n",
            encoding="utf-8",
        )

        metadata_path.write_text(
            json.dumps(
                {
                    "batch": i,
                    "repositories": [repo for repo, _ in batch],
                    "sha256": digest,
                    "model": model,
                },
                indent=2,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

        results.append(result)

    return results


def global_synthesis(batch_results, outdir, model):
    content = "\n\n".join(
        f"===== BATCH {i} =====\n\n{text}"
        for i, text in enumerate(batch_results, start=1)
    )

    print("GENERATE global synthesis")

    result = ollama_generate(
        model,
        GLOBAL_PROMPT.format(content=content),
    )

    output = outdir / "GLOBAL_SUMMARY.md"

    output.write_text(
        "# Global Repository Synthesis\n\n"
        + result
        + "\n",
        encoding="utf-8",
    )

    return output


def main():
    parser = argparse.ArgumentParser(
        description="Hierarchically summarize a corpus of repository READMEs."
    )

    parser.add_argument(
        "input",
        nargs="?",
        default="all-readmes",
        help="Directory containing collected READMEs",
    )

    parser.add_argument(
        "--output",
        default="readme-summary",
        help="Directory for summaries and intermediate results",
    )

    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Ollama model (default: {DEFAULT_MODEL})",
    )

    parser.add_argument(
        "--batch-chars",
        type=int,
        default=60000,
        help="Approximate maximum characters of repository summaries per batch",
    )

    args = parser.parse_args()

    root = Path(args.input)
    outdir = Path(args.output)

    if not root.exists():
        raise SystemExit(f"Input directory does not exist: {root}")

    outdir.mkdir(parents=True, exist_ok=True)

    paths = find_readmes(root)

    print(f"Found {len(paths)} README files.")
    print(f"Model: {args.model}")
    print()

    summaries = []

    for n, path in enumerate(paths, start=1):
        print(f"[{n}/{len(paths)}] ", end="")

        try:
            repo, summary_path = summarize_individual(
                root,
                path,
                outdir,
                args.model,
            )

            summaries.append(
                (repo, read_text(summary_path))
            )

        except Exception as exc:
            print(f"ERROR {path}: {exc}")

    if not summaries:
        raise SystemExit("No summaries were produced.")

    print()
    print(f"Repository summaries available: {len(summaries)}")
    print()

    batches = synthesize_batches(
        summaries,
        outdir,
        args.model,
        args.batch_chars,
    )

    print()
    final_path = global_synthesis(
        batches,
        outdir,
        args.model,
    )

    print()
    print("Finished.")
    print(f"Global summary: {final_path}")


if __name__ == "__main__":
    main()
