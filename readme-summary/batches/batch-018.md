# Batch 18

**Summary**

The *opencode-agent-system* repository is a TypeScript‑based platform designed to build AI agents that can interact with any OpenAI‑compatible language model (such as llama.cpp, vLLM, or Ollama). It provides:

- **LLM client**: Interfaces for connecting to various LLM backends.
- **Tool system**: 16 built‑in tools (e.g., read/write files, shell execution, pattern matching) that agents can invoke.
- **Agent loop**: Implements a dual‑model A* search mechanism to coordinate reasoning and tool usage efficiently.
- **Context‑transfer bridge**: Handles communication between mixture‑of‑experts (MoE) models and dense language models.

The system is built on top of *Effect v4*, ensuring side‑effect‑free, functional operations. It consists of several packages:

| Package | Role |
|---|---|
| `@belarusian/harness` | Core LLM client + agent loop |
| `@belarusian/tools`   | Collection of 16 utility tools for file I/O, shell commands, pattern matching, etc. |
| `@belarusian/agents` | Agent service with skills, sub‑agents, and preset configurations |
| `@belarusian/bridge` | Bridge that manages context transfer between MoE and dense models |

**Installation & Usage**

- **From source**: Run `pnpm install && pnpm build`.
- **As a dependency**: Add the GitHub Packages URL (with an auth token for npm) and then install via `pnpm add @belarusian/harness effect`.

**Quick Start Example**

```bash
opencode-agent run --prompt "Build a REST API for user authentication" \
                    --model "qwen3-coder" \
                    --url "http://localhost:8080/v1"
```

Or using the SDK:

```typescript
import { runAgent } from "@belarusian/harness";
import * as Effect from "effect/Effect";

const result = await Effect.runPromise(
  runAgent({
    config: { baseUrl: "http://localhost:8080/v1", model: "qwen3-coder" },
    messages: [{ role: "user", content: "Build a REST API" }],
    maxSteps: 5,
  }),
);
```

**Testing & Maturity**

- Includes **635 automated tests**, covering all core components (harness, tools, agents, bridge).
- Currently at version **0.1.0** (alpha), indicating it is functional for prototyping but still experimental.

**Key Concepts**

- Dual‑model A* search algorithm
- Effect programming model (Effect v4)
- Modular package architecture (harness, tools, agents, bridge)
- OpenAI‑compatible LLM interoperability

**Keywords**

typescript, agent platform, llm client, tool system, dual-model a*, effect programming, openai compatible, harness, tools, agents, bridge, version 0.1.0, experimental, modular architecture, effect v4, llama.cpp, vllm, ollama, tests (635), mit license.
