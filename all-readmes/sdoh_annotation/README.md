# SDOH Annotation Project

This project implements a complete Social Determinants of Health (SDOH) annotation pipeline, including data augmentation, prompt optimization, and model training phases.

## Project Structure

```
project/
├── augmenting.py           # Data augmentation script
├── prompts.py             # Prompt templates
├── optimize_prompt.py     # Prompt optimization script
├── definition.json        # Label definition file
├── baseline_llm.ipynb     # Baseline model implementation
├── dspy_train.ipynb       # DSPy training workflow
├── dspy_load.ipynb        # DSPy model loading
├── bert_ft.ipynb          # BERT fine-tuning
└── requirements.txt       # Dependency list
```

## 1. Data Preparation and Augmentation

### 1.1 Label Definitions (definition.json)
The project uses a structured JSON file to define the SDOH label system:

  - t1_Homelessness
  - t1_InadequateHousing
  - t1_LackOfAdequateFood
  - t2_FinancialInsecurity
  - t2_HousingInstability
  - t2_MaterialHardship
  - t2_TransportationInsecurity
  - t3_Eviction_absent
  - t3_Eviction_present_history
  - t3_Eviction_present_current
  - t3_Eviction_pending
  - t3_Eviction_mr_history
  - t3_Eviction_mr_current
  - t3_Eviction_hypothetical

Each label includes:
- Detailed definition
- Example sentences
- Usage guidelines

### 1.2 Data Augmentation (augmenting.py)
Two modes are used for data augmentation:

1. MIMIC Mode:
   - Complete rewriting of clinical notes
   - Integration of SDOH label information
   - Maintaining medical accuracy
   - Output limited to 100 words

2. PMC Mode:
   - Insertion of 1-2 relevant sentences into existing notes
   - Ensuring natural integration with context
   - Maintaining narrative coherence

### 1.3 Prompt Optimization (prompts.py & optimize_prompt.py)
Contains three core prompt templates:

1. MIMIC prompts: For complete note rewriting
2. PMC prompts: For contextual insertion
3. Optimization prompts: For refining definitions based on expert feedback

Optimization process:
- Analysis of error case patterns
- Adjustment of definitions based on expert feedback
- Addition of new examples
- Maintaining clarity and accuracy of definitions

## 2. Model Training

### 2.1 DSPy Training (dspy_train.ipynb)
Using the DSPy framework for model training:

1. Data Preparation:
   - Preparing train set and dev set
   - Data preprocessing and formatting

2. Training Process:
   - Configuring DSPy training parameters
   - Implementing custom training logic
   - Model evaluation and optimization

3. Output:
   - Trained model
   - Performance evaluation report
   - Optimized prompts

### 2.2 Open Source Model Fine-tuning

#### BERT Fine-tuning (bert_ft.ipynb)
BERT model fine-tuning for SDOH classification:

1. Data Preparation:
   - Text preprocessing
   - Label encoding
   - Dataset splitting

2. Training Configuration:
   - Learning rate settings
   - Batch size optimization
   - Training epochs adjustment

3. Evaluation Metrics:
   - Accuracy
   - F1 score
   - Confusion matrix

#### Qwen/llama Fine-tuning
Model fine-tuning using Unsloth acceleration:

1. Optimization Features:
   - 2x training speed
   - Reduced memory usage
   - Improved inference efficiency

2. Training Steps:
   - Configuring Unsloth optimizer
   - Implementing LoRA fine-tuning
   - Model evaluation and export

## Usage Instructions

### Environment Setup
```bash
pip install -r requirements.txt
```

### API Key Configuration
Create a .env file and configure:
```
OPENAI_API_KEY=your_key
LANGFUSE_PUBLIC_KEY=your_key
LANGFUSE_SECRET_KEY=your_key
LANGFUSE_HOST=your_host
```

### Running Data Augmentation
```python
python augmenting.py
```

### Running Training
1. Open the corresponding training file in Jupyter Notebook
2. Follow the instructions in the notebook step by step
