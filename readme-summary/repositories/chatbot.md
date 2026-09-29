# chatbot

Summary:

The `chatbot` repository hosts a Bash script designed to simulate conversations among three AI bots—AnalystBot, CreativeBot, and SkepticBot—using IBM's Granite model (`granite3.2:8b`). The simulation generates dynamic, multi-turn dialogues based on user-provided or default prompts (e.g., discussions about AI in education). Responses are saved to specific folders, compiled into a central summary file, logged for progress tracking, and displayed in the terminal using `tee`. The script leverages Ollama to run the Granite model locally, which is an 8 billion parameter decoder-only foundation model trained on diverse datasets including Internet content, academic publications, code, and legal/financial documents. It operates under the Apache 2.0 license.

Key aspects include:
- Distinct personalities of the bots (logical, creative, critical).
- Use of IBM Granite for enhanced response quality.
- Prerequisites: Ollama installation and model pulling, Bash environment, and write permissions.
- Output management via dedicated folders and log files.
- MIT License governing usage.

KEYWORDS:
chatbot repository, conversation simulation, AnalystBot, CreativeBot, SkepticBot, IBM Granite model, Granite3.2:8b, Ollama, decoder-only foundation model, natural language processing, Apache 2.0 license, multi-turn dialogue, starter prompt, terminal output, progress log.
