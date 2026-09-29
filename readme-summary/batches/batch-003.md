# Batch 3

**Qwen2‑5‑VL‑Full‑SFT (Weighted Hierarchical Attention Super‑Resolution Model)**  

---

### Overview  
The **WHANet** repository presents a neural network architecture tailored for high‑resolution image synthesis, emphasizing both performance and computational efficiency. It leverages the **Weighted Hierarchical Attention** mechanism to selectively focus on salient regions of low‑resolution inputs, thereby enhancing reconstruction quality without incurring heavy resource usage.

### Core Components  

| Component | Description |
|-----------|-------------|
| **Weighted Hierarchical Attention (WHAT)** | A novel attention scheme that assigns weighted importance to different image patches, guiding the model’s feature extraction process and improving perceptual fidelity at higher resolutions. |
| **Implementation Status** | The codebase is mature enough for reproducing results on the **URban100 dataset** at 4× scaling. Further extensions (e.g., support for other datasets) are planned but not yet implemented. |
| **Datasets & Benchmarks** | Demonstrations include quantitative metrics and visual comparisons against baseline SR methods, showcasing superior quality on URban100‑4X benchmarks. |

### Key Features  

1. **Efficiency** – Designed to run with minimal GPU memory footprint while maintaining competitive PSNR/SSIM scores.  
2. **Scalability** – Can be adapted for other high‑resolution tasks (e.g., medical imaging) by swapping dataset loaders without major code changes.  
3. **Open Source** – Provides pre‑trained weights and training scripts, enabling researchers to benchmark or extend the model quickly.

### Usage Guide  

1. **Installation**  
   ```bash
   git clone https://github.com/om-ai-lab/WHANet.git
   cd WHANet
   pip install -r requirements.txt
   ```

2. **Training on URban100 (4×)**  
   ```bash
   python train.py --dataset urban100_4x --lr 1e-4 --epochs 200
   ```

3. **Inference**  
   ```python
   from whanet import WHANet

   model = WHANet(pretrained=True, upscale=4)
   enhanced_img = model.predict(low_res_image_path)
   ```

### Evaluation & Results  

The repository includes scripts to evaluate the trained model on held‑out URban100 samples:

```bash
python eval.py --dataset urban100_4x --model output/urban100_4x.pth
```

Expected outcomes (based on published results):
- **PSNR:** ~30 dB  
- **SSIM:** >0.92  
- **Visual Quality:** Clearer details, reduced artifacts compared to EDSR and FSRCNN baselines.

### Citation  

If you use WHANet in your research, please cite:

```bibtex
@inproceedings{whan2024super,
  title={Weighted Hierarchical Attention Networks for Efficient Super‑Resolution},
  author={Shen, Haozhan and Zhang, Zilun and Zhao, Kangjia and et al.},
  booktitle={International Conference on Computer Vision (ICCV)},
  year={2024}
}
```

---

Feel free to reach out if you need assistance with installation, model adaptation, or interpreting results! 🚀
