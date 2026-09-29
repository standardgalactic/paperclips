# EchoVLM

**Summary**

EchoVLM is an official PyTorch implementation of the model described in *“EchoVLM: Dynamic Mixture‑of‑Experts Vision‑Language Model for Universal Ultrasound Intelligence”* (arXiv 2509.14977). Authored by Chaoyin She and Ruifang Lu, the repository provides code to reproduce results from their paper and includes pre‑trained model weights on Hugging Face.

Key features:

- **Model Architecture** – A dynamic mixture‑of‑experts (MoE) vision‑language framework designed for ultrasound image analysis. The MoE enables selective activation of expert subnetworks, improving efficiency and performance.
- **Functionality** – Accepts both single and multiple ultrasound images together with natural‑language queries to generate structured reports or textual descriptions.
- **Usage Example** – Demonstrates how to load the model via `Qwen2VLMOEForConditionalGeneration`, prepare image inputs using `process_vision_info`, and run inference for a single or batch of ultrasound cases.
- **Citation Requirement** – Users must cite the arXiv paper (She et al., 2025) when employing the model in research.

The repository is currently at version 1.0, with future releases planned to incorporate chain‑of‑thought reasoning and reinforcement learning enhancements.

**KEYWORDS:** EchoVLM, dynamic mixture‑of‑experts, vision‑language model, ultrasound intelligence, PyTorch implementation, arXiv:2509.14977, citation required, MoE architecture, image report generation.
