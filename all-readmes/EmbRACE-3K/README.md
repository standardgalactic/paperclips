<h1 align="center">
  <strong><span style="color:#c0392b">Emb</span><span style="color:#27ae60">R</span><span style="color:#2980b9">A</span><span style="color:#f39c12">C</span><span style="color:#8e44ad">E</span><span style="color:#7f8c8d">-3K</span></strong><br>
  Embodied Reasoning and Action in Complex Environments
</h1>

<p align="center">
  <a href="https://mxllc.github.io/EmbRACE-3K/">
    <img src="assets/badge-website.svg" alt="Website">
  </a>
  <a href="https://arxiv.org/pdf/2507.10548">
    <img src="https://img.shields.io/badge/arXiv-PDF-b31b1b" alt="Paper">
  </a>
</p>

---

## 📌 Overview

**<span style="color:#c0392b">Emb</span><span style="color:#27ae60">R</span><span style="color:#2980b9">A</span><span style="color:#f39c12">C</span><span style="color:#8e44ad">E</span><span style="color:#7f8c8d">-3K</span>** is a large-scale dataset for embodied vision-language reasoning. It includes over **3,000** language-guided tasks and **26,000** decision steps across diverse, photorealistic environments built with Unreal Engine.

Recent vision-language models (VLMs) perform well on offline image and video tasks but struggle in **interactive** and **embodied** settings. In **closed-loop** environments, agents act from a first-person view where each decision alters future observations. Even advanced models like **GPT-4o**, **Claude 3.5 Sonnet**, and **Gemini 2.5 Pro** show clear limitations in **spatial reasoning** and **long-horizon planning**.

**<span style="color:#c0392b">Emb</span><span style="color:#27ae60">R</span><span style="color:#2980b9">A</span><span style="color:#f39c12">C</span><span style="color:#8e44ad">E</span><span style="color:#7f8c8d">-3K</span>** provides a systematic benchmark to evaluate these limitations, and training on this dataset helps mitigate key challenges in step-wise embodied reasoning.

Each task provides:

- 👁️ Egocentric visual observations  
- 📝 High-level task instructions  
- 🕹 Grounded action sequences  
- 💬 Step-level natural language rationales

We evaluate models on three core reasoning skills:

- 🧭 **Exploration**
- 🧠 **Dynamic Spatial-Semantic Reasoning**
- 🎯 **Multi-stage Goal Execution**

In zero-shot evaluations, all models perform under **20%** success rate, revealing significant gaps. Fine-tuning **Qwen2.5-VL-7B** with supervised learning and reinforcement learning yields notable improvements across all task types.

---

## 🔁 Step-by-Step Closed-Loop Reasoning

This demo shows how a fine-tuned **Qwen2.5-VL-7B** agent reasons and acts step by step in a closed-loop setting, guided by egocentric perception and language-based reasoning.

<div align="center">
  <img src="assets/qwen_ft.gif" width="100%">
</div>

---

## 📊 Dataset Overview

An overview of <span style="color:#c0392b">Emb</span><span style="color:#27ae60">R</span><span style="color:#2980b9">A</span><span style="color:#f39c12">C</span><span style="color:#8e44ad">E</span><span style="color:#7f8c8d">-3K</span>, consisting of **3.1k** tasks and **26k** decision steps across diverse environments. Tasks involve multi-step grounded reasoning and perceptual decision making.

<div align="center">
  <img src="assets/teaser.png" width="100%">
</div>

---

## 🛠 Dataset Construction Pipeline

The dataset is constructed in four stages:

1. Sampling diverse 6-DoF egocentric views  
2. Generating task instructions using **Gemini**  
3. Collecting high-quality human demonstrations  
4. Annotating each action with step-level rationales

<div align="center">
  <img src="assets/pipeline.png" width="100%">
</div>

---

## 📂 Dataset and Code

Coming soon!

---

## 📖 Citation

If you find our work helpful, please cite:

```bibtex
@article{lin2025embrace3k,
  title={EmbRACE-3K: Embodied Reasoning and Action in Complex Environments},
  author={Lin, Mingxian and Huang, Wei and Li, Yitang and Jiang, Chengjie and Wu, Kui and Zhong, Fangwei and Qian, Shengju and Wang, Xin and Qi, Xiaojuan},
  journal={arXiv preprint arXiv:2507.10548},
  year={2025}
}
