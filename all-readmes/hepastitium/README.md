# Hepastitium

**Prerogative Posing**

![Bandwidth compression](bandwidth-compression.jpg)

Hepastitium is a research repository containing source material, experimental
utilities, and the LaTeX source for *A Relativistic Theory of Longevity*. It is
not a single software package, so there is no repository-wide build step.

## Clone the repository

```bash
git clone https://github.com/standardgalactic/hepastitium.git
cd hepastitium
```

## Build the monograph

The reproducible document target is
`monograph/relativistic_longevity.tex`. It uses standard LaTeX packages,
including AMS math, TikZ, `geometry`, `enumitem`, `booktabs`, and
`hyperref`.

On Debian or Ubuntu, install a suitable TeX Live environment:

```bash
sudo apt update
sudo apt install texlive-latex-extra texlive-pictures
```

Then compile from the repository root:

```bash
cd monograph
pdflatex -interaction=nonstopmode -halt-on-error relativistic_longevity.tex
pdflatex -interaction=nonstopmode -halt-on-error relativistic_longevity.tex
```

The second pass resolves cross-references. The resulting document is
`monograph/relativistic_longevity.pdf`.

If `latexmk` is installed, the equivalent command is:

```bash
cd monograph
latexmk -pdf -interaction=nonstopmode -halt-on-error relativistic_longevity.tex
```

## Optional text-extraction utility

`extract-text.py` extracts text from PDF and MHTML files in the current
directory. It requires Python 3, Beautiful Soup, and PyMuPDF:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install beautifulsoup4 PyMuPDF
python extract-text.py
```

The script writes a `.txt` file beside each input file. Run it only in a
directory whose PDFs or MHTML files you intend to process.

## Optional local-summary utilities

`get-chunksize.sh` reports proposed chunk sizes for text files:

```bash
bash get-chunksize.sh
```

`get-summaries.sh` recursively summarizes text files with a local Ollama
model. It currently expects the model `vanilj/phi-4`:

```bash
ollama pull vanilj/phi-4
bash get-summaries.sh
```

This creates or updates `progress.log` and `detailed-summary.txt`. Because
the script recursively processes `.txt` files and invokes a local language
model for every chunk, review it before running it on the complete corpus.

The remaining small programs are independent language experiments rather than
parts of a common build. Compile or run them with their respective toolchains.
