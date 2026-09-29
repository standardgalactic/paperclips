# PKDiff

**Summary**

PKDiff is a PyTorch‑based toolkit designed for training and evaluating deep learning models on multimodal remote sensing segmentation tasks (often referred to as DDP – Distributed Data Parallel). It supports both single‑machine multi‑GPU setups (e.g., 4 GPUs) and distributed multi‑machine configurations, leveraging **PyTorch’s DistributedDataParallel** framework. Key features include:

- **Learning Rate Scheduling:** Linear warmup followed by cosine decay.
- **Parameter‑Grouped Learning Rates:** Allows different learning rates per model parameter group.
- **Distributed Evaluation Aggregation:** Summarizes metrics across multiple nodes for consistent evaluation results.
- **NVML GPU Information Printing:** Provides detailed GPU utilization and status via NVML.

The repository contains a structured directory layout:

```
repo_root/
├── train.py               # Main training script entry point
├── networks/network.py   # Defines NetworkConfig & Network classes
├── trainer.py            # Trainer class with distributed training logic
├── utils1.py              # Contains data paths, constants (train_ids, test_ids, BATCH_SIZE, etc.)
├── utils/evaluation.py    # Evaluator, denoising utilities, and segmentation metrics
└── eval_patch_dataset.py  # Custom dataset loader for patch‑based evaluation
requirements.txt          # Lists all Python dependencies (rasterio, affine, torch, etc.)
```

**Implementation Status & Maturity**

- The project is currently in an “organizing and supplementing” phase; core functionality (training scripts, network definitions) is functional but not yet fully documented or polished.
- No release version has been published; the README explicitly notes ongoing development.

**Relationships**

- PKDiff targets multimodal remote sensing segmentation tasks, which often involve integrating optical imagery with LiDAR or SAR data. It does not directly interface with other repositories unless they provide compatible dataset formats (e.g., rasterio‑compatible GeoTIFFs).
- The codebase is intended to complement existing PyTorch distributed training patterns rather than replace them.

**Unusual/Important Claims**

- Emphasis on **parameter‑grouped learning rates**, a non‑standard approach that may improve convergence for highly imbalanced model components.
- Integration of **NVML GPU information printing**, enabling real‑time monitoring of resource usage across nodes—a feature not commonly found in standard PyTorch training scripts.

**KEYWORDS:**

multimodal remote sensing segmentation, DDP (Distributed Data Parallel), PyTorch, distributed training, parameter grouped learning rates, NVML GPU info, rasterio, affine, evaluation metrics, patch dataset loader.
