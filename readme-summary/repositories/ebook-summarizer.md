# ebook-summarizer

**Summary**

The *ebook-summarizer* repository implements a local‑first pipeline for summarizing a large archive (~500) of early 2000s technical computing books (primarily PDF and CHM formats). It extracts CHM files into hierarchical HTML/PDF structures, cleans the resulting text chunks, and uses IBM Granite’s `granite4.1:3b` model via Ollama to generate per‑book Markdown summaries that separate historically specific implementation details from durable technical concepts. The pipeline is designed for large books by chunking content (overlapping segments), recursively summarizing intermediate results if needed, and checkpointing outputs so interrupted runs can resume without re‑generating completed chunks. Requirements include Linux/WSL, Python 3, Ollama, IBM Granite model, and poppler utilities. The repository tracks only processing scripts and derived summaries, keeping the source library (PDFs/CHMs) out of version control to maintain a clear separation between raw artifacts and navigational indices.

**KEYWORDS:** ebook summarizer, technical computing books, CHM extraction, Ollama, IBM Granite, local-first pipeline, chunked summarization, historical preservation, Linux, Python.
