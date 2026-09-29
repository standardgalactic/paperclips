# raglite

**Improving Retrieval‑Augmented Generation (RAG) with an Optimal Query Adapter**

Below is a concise guide on how to enhance your RAG pipeline using the `update_query_adapter` function from the **raglite** library. This approach helps ensure that every vector search leverages a well‑tuned query adapter, which can improve retrieval accuracy and overall model performance.

### Step‑by‑Step Guide

1. **Insert Evaluation Data**
   ```python
   from raglite import insert_evals

   # Load 100 evaluation examples with your configuration (my_config)
   insert_evals(num_evals=100, config=my_config)
   ```
   *Purpose:* Populate the knowledge base with a representative set of questions and corresponding answers that will be used for training the query adapter.

2. **Update the Query Adapter**
   ```python
   from raglite import update_query_adapter

   # Apply an optimal query adapter to all future vector searches
   update_query_adapter(config=my_config)
   ```
   *Purpose:* By updating the query adapter after inserting evaluation data, you ensure that subsequent retrievals are optimized for the specific domain and quality of your training examples.

### Evaluation of Retrieval & Generation

If you have installed the `ragas` extra (recommended), you can evaluate both retrieval and generation steps using **Ragas**:

```python
from raglite import answer_evals, evaluate, insert_evals

# Re‑insert evaluation data if needed
insert_evals(num_evals=100, config=my_config)

# Answer a subset of evaluations
answered_evals_df = answer_evals(num_evals=10, config=my_config)

# Evaluate retrieval and generation quality
evaluation_df = evaluate(answered_evals_df, config=my_config)
```

### Running an MCP Server

RAGLite includes an **MCP (Model Context Protocol) server** that exposes a `search_knowledge_base` tool. Follow these steps:

1. **Install Claude Desktop**
   - Download and install [Claude desktop](https://claude.ai/download).

2. **Install uv for the MCP Server**
   ```sh
   pip install uv
   ```

3. **Configure Claude to Use uv**
   ```sh
   raglite \
       --db-url sqlite:///raglite.db \
       --llm llama-cpp-python/bartowski/Llama-3.2-3B-Instruct-GGUF/*Q4_K_M.gguf@4096 \
       --embedder llama-cpp-python/lm-kit/bge-m3-gguf/*F16.gguf@1024 \
       mcp install
   ```
   *Purpose:* This command installs the MCP server with your chosen LLM and embedding model.

4. **Start Claude Desktop**
   - When you launch Claude desktop, a 🔨 icon will appear in the bottom‑right corner, indicating successful connection to the MCP server.
   - The application can now suggest or explicitly request use of the `search_knowledge_base` tool for retrieval tasks.

### Serving a Customizable ChatGPT‑Like Frontend

If you’ve installed the **chainlit** extra, you can serve an interactive frontend with:

```sh
raglite chainlit
```

- **Configuration Options:**
  ```sh
  raglite \
      --db-url sqlite:///raglite.db \
      --llm llama-cpp-python/bartowski/Llama-3.2-3B-Instruct-GGUF/*Q4_K_M.gguf@4096 \
      --embedder llama-cpp-python/lm-kit/bge-m3-gguf/*F16.gguf@1024 \
      chainlit
  ```
  *Or* for API‑based LLMs:
  ```sh
  OPENAI_API_KEY=sk-... raglite --llm gpt-4o-mini --embedder text-embedding-3-large chainlit
  ```

- **Deployment Targets:** The application can be deployed to web, Slack, or Teams via the respective integration options provided by Chainlit.

### Contributing Guidelines

#### Prerequisites

1. **SSH Key & GitHub Account**
   - Generate an SSH key and add it to your GitHub account.
2. **Docker Desktop**
   - Install Docker Desktop for seamless containerization of dependencies.
3. **VS Code (or PyCharm) with Dev Containers**
   - Set up a development environment using VS Code’s Dev Container extension or JetBrains’ equivalent.

#### Development Environments

- **GitHub Codespaces:** Click “Open in GitHub Codespaces” to start developing directly from the web UI.
- **VS Code Dev Container (with container volume):** Clone and open the repo in VS Code, then run:
  ```sh
  uv sync --python 3.10 --all-extras
  source .venv/bin/activate
  pre-commit install --install-hooks
  ```
- **PyCharm Dev Container:** Follow similar steps to set up a PyCharm environment with containerized dependencies.

#### Development Workflow

- Use **Poe the Poet** tasks (`poe`) for quick task execution.
- Install runtime or development packages via:
  ```sh
  uv add {package} [--dev]
  ```
- Upgrade all dependencies and create git tags using Commitizen:
  ```sh
  cz bump
  ```

### Star History

A visual representation of the project’s star history (via [Star‑History](https://star-history.com/)):

<a href="https://star-history.com/#superlinear-ai/raglite&Timeline">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=superlinear-ai/raglite&type=Timeline&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=superlinear-ai/raglite&type=Timeline" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=superlinear-ai/raglite&type=Timeline" />
 </picture>
</a>

---

**Feel free to reach out for further assistance or clarification on any of these steps!**
