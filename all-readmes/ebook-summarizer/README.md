# Local Technical Library Summarizer

A local-first pipeline for extracting, processing, and summarizing a large archive of technical computing books using Ollama and IBM Granite.

The source collection contains roughly 500 programming and systems books, primarily from the early 2000s. It includes material on Unix and Linux, Java and J2EE, C and C++, Python, Perl, PHP, XML, Oracle, SQL, Windows administration, networking, security, and related subjects.

Many of the books were distributed as Microsoft Compiled HTML Help (`.chm`) files rather than ordinary PDFs. Once extracted, those CHM files expand into tens or hundreds of thousands of HTML pages, images, indexes, stylesheets, and support files.

This repository contains the machinery for working with that collection without putting the collection itself in Git.

## The basic idea

The pipeline is:

```text
        original library
          PDF / CHM
              │
              ▼
       extract CHM files
              │
              ▼
      HTML / PDF documents
              │
              ▼
        text extraction
              │
              ▼
      cleanup + deduplication
              │
              ▼
          text chunks
              │
              ▼
      Granite chunk summaries
              │
              ▼
      hierarchical reduction
              │
              ▼
       per-book Markdown
            summary
```

Everything is performed locally.

No remote language-model API is required.

## Why?

Old technical books occupy an interesting position between documentation and history.

A book about Linux, Java, XML, Oracle, Windows, or networking from 2001–2004 contains at least two different kinds of information:

1. technical ideas that remain useful;
2. implementation details tied to a particular historical software environment.

A useful summary should preserve that distinction.

The summarizer therefore asks the model not to silently modernize the source. Instead, it explicitly separates historically specific material from durable concepts.

For example, an obsolete API may no longer be useful as an API, while the architectural problem it was designed to solve may still be worth understanding.

## Library structure

After extraction, the working library has approximately this structure:

```text
extracted-books/
├── Some.Book.pdf
├── Another.Book.pdf
│
├── Some.Extracted.CHM/
│   ├── index.html
│   ├── toc.html
│   ├── chapter01/
│   │   ├── page001.html
│   │   ├── page002.html
│   │   └── ...
│   ├── images/
│   └── ...
│
└── Another.Extracted.CHM/
    └── ...
```

Each immediate directory represents one extracted CHM book.

Each immediate PDF represents one PDF book.

The current collection contains approximately:

```text
341 extracted CHM books
153 PDF books
-----------------------
494 books
```

The extracted working tree contains more than 120,000 files.

For that reason, `extracted-books/` is deliberately excluded from Git.

## Summarization

The current summarizer uses:

```text
granite4.1:3b
```

through Ollama.

Large books cannot usefully be summarized in a single model invocation, so summarization uses a map/reduce-style process.

A book is first divided into overlapping chunks:

```text
Book
 │
 ├── Chunk 001 ──► summary 001
 ├── Chunk 002 ──► summary 002
 ├── Chunk 003 ──► summary 003
 │       ...
 └── Chunk N   ──► summary N
                       │
                       ▼
              intermediate reduction
                       │
                       ▼
                  final summary
```

If the intermediate summaries are themselves too large, they are recursively summarized before the final synthesis.

This permits books substantially larger than the model context window to be processed while retaining information from across the book.

## Checkpointing

Model output is checkpointed as it is generated.

Intermediate files are stored under:

```text
.granite-cache/
```

If processing is interrupted after, for example,

```text
[37/74] Granite ...
```

the first 36 completed summaries do not need to be generated again.

On restart, the summarizer can continue with the remaining chunks.

The cache is intentionally excluded from Git.

## Final summaries

Completed summaries are Markdown documents with metadata describing their provenance:

```yaml
---
title: "Understanding the Linux Kernel"
source: ".../Understanding the Linux Kernel.pdf"
format: "pdf"
model: "granite4.1:3b"
chunks: 74
---
```

The generated summary then uses a common structure:

```text
What this book is about

Core concepts

Important techniques

Architecture and mental model

Historically specific material

Durable ideas

Book outline

Key takeaways
```

The resulting Markdown summaries are small enough to keep in Git even though their source library is not.

## Requirements

The pipeline currently assumes:

* Linux or WSL
* Python 3
* Ollama
* IBM Granite available through Ollama
* Poppler's `pdftotext`
* `libchm-bin` for CHM extraction

On Debian/Ubuntu:

```bash
sudo apt update
sudo apt install poppler-utils libchm-bin
```

Install or pull the model with Ollama as appropriate, then verify that it is available:

```bash
ollama list
```

The expected model is:

```text
granite4.1:3b
```

## Running the summarizer

A small trial run is recommended first:

```bash
python3 -u ./granite_summarize.py \
    ./extracted-books \
    --model granite4.1:3b \
    --limit 1
```

Then try several books:

```bash
python3 -u ./granite_summarize.py \
    ./extracted-books \
    --model granite4.1:3b \
    --limit 10 \
    |& tee granite-run.log
```

Once the output is satisfactory, remove the limit to process the complete library.

## Repository policy

This repository tracks the processing machinery and compact derived artifacts, not the source corpus.

In particular:

```text
tracked                         ignored
─────────────────────────────────────────────────
Python scripts                  extracted-books/
CHM extraction scripts          *.pdf
README                          *.chm
.gitignore                      *.iso
final Markdown summaries        .granite-cache/
                                diagnostic output
                                logs
```

This keeps the repository small and makes the distinction between source material, temporary computation, and derived output explicit.

## What this repository is really about

The immediate task is book summarization, but the larger experiment is archival compression.

A technical library can be represented at several resolutions:

```text
original artifact
      ↓
extracted document structure
      ↓
normalized text
      ↓
local chunk summaries
      ↓
book-level summaries
      ↓
library-level index
```

Each level discards information, but each also makes a different kind of traversal possible.

The original books remain the authoritative artifacts. The summaries are not replacements for them. They are a navigational layer: a way to determine what is in the collection, which books contain a relevant idea, what material is historically bounded, and where returning to the original text is worthwhile.

That makes the project less a conversion of books into summaries than the construction of an interface over a technical library.

