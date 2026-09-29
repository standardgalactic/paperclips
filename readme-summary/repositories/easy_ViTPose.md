# easy_ViTPose

**Summary**

`easy_ViTPose` provides a ready‑to‑use implementation of the state‑of‑the‑art **ViTPose** model (Y. Xu et al., 2022) for accurate 2D human pose estimation with 25 keypoints, including feet. It supports inference on images, videos, and webcams via command‑line scripts (`inference.py`) or programmatically through the `VitInference` class. The repository offers four model sizes (s, b, l, h) in ONNX/TensorRT/PyTorch formats, with performance benchmarks showing:

- **ViTPose-s**: ~250 fps on GTX1080ti (TensorRT)
- **ViTPose-b**: ~125 fps
- **ViTPose-l**: ~45 fps
- **ViTPose-h**: ~24.5 fps

Key features include:

- Support for Apple silicon via MPS.
- Integration of the SORT object tracker to maintain multi‑pose identification in videos.
- Ability to save output images, videos, and JSON files containing keypoints (y, x, confidence) and a skeleton reference mapping.
- Installation instructions with optional `requirements.txt` packages; models must be downloaded from HuggingFace.

The project is built on the fork of **jaehyunnn/ViTPose_pytorch** and references the original **ViTAE‑Transformer/ViTPose** implementation, incorporating SORT tracking code (abewley/sort). Current TODOs involve optimizing tracker usage for single‑pose videos, enhancing inference speed with parallel batched runs, and refining confidence masking on skeleton drawings.

**KEYWORDS:**
easy_ViTPose
human pose estimation
ViTPose model
25 keypoints
COCO + feet dataset
ONNX/TensorRT/PyTorch models
Apple MPS support
SORT tracking algorithm
image/video/webcam inference
benchmark performance (fps)
installation guide
GitHub repository fork
jaehyunnn ViTPose_pytorch
abewley sort
