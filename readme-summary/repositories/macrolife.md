# macrolife

**Summary**

Macrolife provides a minimal, reproducible Docker container that bundles a curated collection of reduced‑resolution images (≈123 MB) derived from larger source PNGs via ImageMagick’s `-resize 50%`. The repository includes the `images/` directory with processed assets and separate `source-images/` for full‑resolution originals (excluded from Git). It ships a prebuilt Docker image (`mechachleopteryx/macrolife:latest`) on Docker Hub, allowing quick interaction without local build. Inside the container, ImageMagick, libvips, FFmpeg, and Python 3 enable basic image conversion, resizing, compositing, filtering, and scripting for higher‑level pipelines. The repository structure isolates workflow metadata (`workflow.json`), checkpoint provenance (SHA‑256 digest of `v1-5-pruned-emaonly.ckpt`), and excludes large source files from Git to keep the clone practical while preserving reproducibility through Dockerfile definitions.

**KEYWORDS:**
macrolife
Docker container
image processing tools
ImageMagick
libvips
FFmpeg
Python scripting
reduced‑resolution image collection
full-resolution source images (excluded from Git)
workflow metadata (workflow.json)
checkpoint provenance (SHA-256 digest)
minimal reproducible environment
