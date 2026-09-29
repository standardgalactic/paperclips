# MonoViT

**RoboDepth Challenge Team – MonoViT Evaluation Summary**

Below is a concise overview of the evaluation results for the MonoViT model (and related models) on the KITTI dataset, as reported by the RoboDepth Challenge Team. The tables include key performance metrics such as depth estimation error and other relevant statistics.

### Model Performance Table

| Model Name                | Metric Type | MAE (meters) | RMSE (meters) |
|---------------------------|-------------|--------------|---------------|
| **MonoViT**               | Mono        | 0.099        | 0.106         |
| [HR-Depth]()              | Mono        | 0.112        | 0.121         |
| [DIFFNet<sub>HRNet</sub>]() | Mono        | 0.102        | 0.111         |
| ManyDepth<sub>single</sub>() | Mono        | 0.123        | 0.135         |
| FSRE-Depth               | Mono        | 0.109        | 0.128         |
| MonoViT<sub>MPViT+HR</sub>() | Mono      | 0.090        | 0.097         |

**Interpretation:**  
MonoViT demonstrates the lowest MAE (Mean Absolute Error) and RMSE (Root Mean Square Error) among all listed models, indicating superior robustness in depth estimation tasks on the KITTI dataset.

### Key Points

- **Robustness Claim:** The RoboDepth Challenge Team highlights MonoViT's outstanding robustness based on these evaluation results.
- **Dataset Details:**  
  - The full KITTI raw data (≈175 GB) can be downloaded via a provided script.  
  - Default settings assume conversion of `.png` images to JPEG with chroma subsampling `2x2,1x1,1x1`. Adjustments are required for different OS versions.
- **Training Instructions:**  
  - Pretrained ImageNet-1K model (mpvit_small.pth) must be downloaded and placed in the appropriate directory.  
  - Training scripts (`train.py`) require specifying model name and learning rate; custom dataloaders can be implemented by inheriting `MonoDataset`.
- **GPU Usage:** The code is designed for single GPU execution, with environment variable `CUDA_VISIBLE_DEVICES` used to select a specific device.
- **Evaluation Options:**  
  - Use `evaluate_depth.py --load_weights_folder ./tmp/mono_model/models/weights_19 --eval_mono` for standard Eigen split.  
  - Additional splits (`eigen_benchmark`, `benchmark`) are available via the `--eval_split` flag, reflecting different ground truth sources.

### Contact Information

For any inquiries or further assistance, please reach out to:

**zhaocqilc@gmail.com**

---

This summary provides a clear snapshot of MonoViT's performance relative to other depth estimation models on the KITTI dataset, emphasizing its robustness and efficiency.
