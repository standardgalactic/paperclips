# CXReasonBench

**Summary**

The CXReasonBench repository provides a benchmark specifically designed to evaluate the ability of Large Vision‑Language Models (LVLMs) to perform **structured diagnostic reasoning on chest X-ray images**. It consists of two core components:

1. **CheXStruct** – an automated pipeline that extracts structured clinical information from raw chest X-rays. The system performs:
   - Anatomical segmentation,
   - Derivation of key landmarks and diagnostic measurements (e.g., lung opacity, heart size),
   - Application of clinical thresholds based on established medical guidelines.

2. **CXReasonBench** – a multi‑path, multi‑stage evaluation framework that tests models’ reasoning capabilities across 12 diagnostic tasks using 18,988 question‑answer pairs drawn from 1,200 annotated cases (each case may involve up to four visual inputs). The benchmark assesses:
   - Visual grounding of answers,
   - Correct application of diagnostic indices,
   - Generalization ability beyond the training data.

The README emphasizes that existing benchmarks typically only measure final diagnostic predictions but fail to capture whether models engage in clinically meaningful reasoning. Empirical results show that even state‑of‑the‑art LVLMs exhibit limited structured reasoning and poor generalization on this benchmark, underscoring its importance for advancing medical AI safety.

**KEYWORDS:** CXReasonBench, CheXStruct, chest X-ray analysis, structured diagnostic reasoning, Large Vision-Language Models, multimodal evaluation framework, clinical thresholds, visual grounding.
