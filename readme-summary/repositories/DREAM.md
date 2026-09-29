# DREAM

**Summary**

DREAM (Drafting with Refined Target Features and Entropy‑Adaptive Cross‑Attention Fusion for Multimodal Speculative Decoding) is an open‑source repository that implements a multimodal speculative decoding framework built on top of the Vicuna‑7B model. Its core purpose is to enable generation of longer, more coherent drafts by:

* **Allocating model weights across multiple GPUs** – allowing models larger than a single GPU’s memory to be loaded and run in parallel.
* **Generating training data via `dream.ge_data.allocation`**, which prepares datasets for downstream fine‑tuning or inference.
* **Training an auto‑regression head using DeepSpeed** with configurable parameters (`ds_config.json`, `tmpdir`, `cpdir`, `configpath`) to optimize performance on high‑performance compute environments.

The repository provides:

* A web UI (`dream.application.webui`) for interactive access, which automatically handles multi‑GPU weight allocation.
* Scripts for **training**, **evaluation** (via MT‑bench), and **inference** on custom models.
* Documentation of dependencies (`pip install -r requirements.txt`) and a note that the project builds upon earlier works such as Medusa, EAGLE, and FastChat.

The README explicitly states that DREAM is still an experimental implementation; results may vary based on hardware (GPU memory, compute resources) and model size. The codebase is designed for researchers interested in multimodal LLMs who wish to push beyond single‑GPU limits while maintaining high quality through entropy‑adaptive cross‑attention fusion.

**KEYWORDS:**
DREAM
multimodal decoding
LLaVA
Vicuna-7B
multi-GPU weight allocation
DeepSpeed training
MT-bench evaluation
open-source LLM research
