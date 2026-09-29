# VidEgoVLM

Below is a concise, step‑by‑step guide to running the provided scripts for both GRPO and SFT training on multimodal tasks using Qwen2.5‑VL model.

---

## 📦 Environment Setup

1. **Clone & Install Dependencies**  
   ```bash
   git clone https://github.com/om-ai-lab/open-r1-multimodal.git
   cd open-r1-multimodal
   pip install -r requirements.txt
   ```

2. **Install LLaMA‑Factory (for SFT)**  
   ```bash
   git clone https://github.com/hiyouga/LLaMA-Factory.git
   cd LLaMA-Factory
   pip install -e ".[torch,metrics]"
   ```

3. **Download Provided Datasets**  
   *For GRPO:*  
   ```bash
   wget https://huggingface.co/datasets/omlab/VLM-R1/resolve/main/lisa-test.zip
   unzip lisa-test.zip -d ./data/
   ```
   *For SFT (GUI‑Testing Arena):*  
   ```bash
   wget https://huggingface.co/datasets/songjah/GTArena-UI-Defects/resolve/id/9e6c8f5a3b1c4e7e2d0c9f3e5c6a7b8.zip -O ./data/gta.zip
   unzip ./data/gta.zip -d ./data/
   ```

---

## 🚀 Running GRPO Training

### 1. Basic Command (Single‑Node)

```bash
cd src/open-r1-multimodal

torchrun --nproc_per_node="8" \
    --nnodes="1" \
    --node_rank="0" \
    --master_addr="127.0.0.1" \
    --master_port="12346" \
  src/open_r1/grpo_rec.py \
    --deepspeed local_scripts/zero3.json \
    --output_dir output/$RUN_NAME \
    --model_name_or_path Qwen/Qwen2.5-VL-3B-Instruct \
    --dataset_name data_config/rec.yaml \
    --image_root ./data/lisa-test/images \  # adjust path as needed
    --max_prompt_length 1024 \
    --num_generations 8 \
    --per_device_train_batch_size 8 \
    --gradient_accumulation_steps 2 \
    --logging_steps 1 \
    --bf16 \
    --torch_dtype bfloat16 \
    --data_seed 42 \
    --report_to wandb \
    --gradient_checkpointing false \
    --attn_implementation flash_attention_2 \
    --num_train_epochs 2 \
    --run_name $RUN_NAME \
    --save_steps 100 \
    --save_only_model true \
    --freeze_vision_modules false
```

### 2. Multi‑Node Training (Optional)

If you have multiple GPUs, refer to the provided `multinode_training_demo.sh` script for proper node configuration.

---

## 🤖 Running SFT with LLaMA‑Factory

1. **Prepare Dataset**  
   Place the downloaded dataset files in:
   - `LLaMA-Factory/data/mllm_rec_json.json`
   - `LLaMA-Factory/examples/train_full/qwen2_5_vl_full_sft.yaml`

2. **Train SFT Model**  
   ```bash
   llamafactory-cli train examples/train_full/qwen2_5_vl_full_sft.yaml
   ```

### For Your Own Data

1. **Prepare JSONL Files** (example format shown below).  
   Each line should be a valid JSON object with:
   - `id`: unique identifier.
   - `image`: path to the image relative to your specified folder(s).
   - `conversations`: list of messages where the first is from “human” and second from “gpt”.

   ```json
   {
     "id": 1,
     "image": "./data/lisa-test/images/000001.png",
     "conversations": [
       {"from": "human", "value": "<image>What number of purple metallic balls are there?"},
       {"from": "gpt", "value": "0"}
     ]
   }
   ```

2. **Run with Custom Paths**  
   ```bash
   torchrun --nproc_per_node="8" \
    --nnodes="1" \
    --node_rank="0" \
    --master_addr="127.0.0.1" \
    --master_port="12345" \
  src/open_r1/grpo_jsonl.py \
    --output_dir output/$RUN_NAME \
    --model_name_or_path Qwen/Qwen2.5-VL-3B-Instruct \
    --deepspeed local_scripts/zero3.json \
    --dataset_name <your_dataset_name> \
    --data_file_paths ./path/to/data1.jsonl:/path/to/data2.jsonl \  # multiple files separated by ":"
    --image_folders ./path/to/images1:./path/to/images2: ... \   # multiple folders separated by ":"
    ...
   ```

---

## 📊 Evaluation

To evaluate the model on a held‑out set:

```bash
cd src/eval

# For GRPO (Grounded Reasoning Open Prompt)
torchrun --nproc_per_node="X" test_rec_r1.py  # X = number of GPUs you have.

# For SFT (Stable Fine‑Tuning)
torchrun --nproc_per_node="X" test_rec_baseline.py
```

---

## 🎉 Acknowledgements

We thank the following projects for their open‑source contributions:

- DeepSeek R1, Open‑R1, QwenVL, Open‑R1‑Multimodal  
- RefCOCO & RefGTA (for grounding benchmarks)  
- LLaMA‑Factory (for SFT training utilities)  
- OVDEval (for evaluation scripts)

---

## 📄 Citation

If you use this work, please cite:

```bibtex
@misc{shen2025vlmr1,
  author       = {Shen, Haozhan and Zhang, Zilun and Zhao, Kangjia and Zhang, Qianqian and Xu, Ruochen and Zhao, Tiancheng},
  title        = {VLM-R1: A stable and generalizable R1-style Large Vision-Language Model},
  howpublished = {\url{https://github.com/om-ai-lab/VLM-R1}},
  note         = {Accessed: 2025-02-15},
  year         = {2025}
}
```

---

Feel free to reach out if you encounter any issues or have questions! 🚀
