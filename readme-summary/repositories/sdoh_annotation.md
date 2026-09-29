# sdoh_annotation

**Summary**

The SDOH Annotation Project provides a comprehensive pipeline for annotating Social Determinants of Health (SDOH) within clinical documentation. It includes:

- **Label Definitions**: A JSON (`definition.json`) that enumerates specific SDOH categories (e.g., homelessness, financial insecurity) with detailed definitions and usage guidelines.
  
- **Data Augmentation**: Two modes—**MIMIC Mode** for rewriting entire notes while preserving medical accuracy, and **PMC Mode** for inserting concise sentences into existing texts to enrich context.

- **Prompt Optimization**: Three template prompt sets (MIMIC, PMC, Optimization) designed to guide language models in accurately incorporating SDOH labels. The optimization process iteratively refines prompts based on expert feedback and error patterns.

- **Model Training**: Utilizes the DSPy framework for training a model capable of classifying SDOH from clinical notes, along with BERT fine-tuning scripts that optimize performance metrics such as accuracy and F1 score. Additionally, it supports Qwen/llama models via Unsloth acceleration for faster and more efficient training.

- **Implementation Details**: The repository contains Python scripts (`augmenting.py`, `optimize_prompt.py`) and Jupyter notebooks (`baseline_llm.ipynb`, `dspy_train.ipynb`, `bert_ft.ipynb`) that guide users through environment setup, API key configuration, data augmentation execution, and model training procedures.

The project is designed to be modular and extensible, allowing integration with existing clinical documentation systems while maintaining high interpretability and accuracy in SDOH annotation. It currently supports both open-source models (BERT) and accelerated fine-tuning options (Qwen/llama via Unsloth).

**KEYWORDS:**
SDOH annotation pipeline, Social Determinants of Health, data augmentation, prompt optimization, DSPy framework, BERT fine-tuning, Unsloth acceleration, clinical documentation, label definitions, JSON configuration.
