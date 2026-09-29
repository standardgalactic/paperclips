# @belarusian/agent-system

![Version](https://img.shields.io/badge/version-0.1.0-blue)
[![Tests](https://img.shields.io/badge/tests-635_passing-brightgreen)](https://github.com/belarusian/opencode-agent-system/actions)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## What Is This?

A self-contained TypeScript agent platform: LLM client, tool system, agent loop with dual-model A* search, and a context-transfer bridge. Extract the pieces you need or use them all together.

Built on [Effect v4](https://effect.website), runs against any OpenAI-compatible LLM server (llama.cpp, vLLM, Ollama, etc.).

## Repository Management Script

Use the built-in management script for common lifecycle operations:

```bash
scripts/manage.sh <command>
```

### Commands

- `clean` – remove build artifacts and local caches
- `build` – install deps and build all packages
- `test` – run test suites
- `typecheck` – run type checks
- `run <mode> [-- ...args]` – run in supported modes (`cli`, `bridge`, `dev`)
- `release` – build and run release packaging when available
- `version <kind>` – bump version (`bump`, `minor`, `major`)

### Examples

```bash
scripts/manage.sh clean
scripts/manage.sh build
scripts/manage.sh run cli -- --help
scripts/manage.sh run bridge -- --help
scripts/manage.sh version minor
```

## Packages

| Package | Purpose |
|---|---|
| `@belarusian/harness` | LLM client + agent loop (self-contained) |
| `@belarusian/tools` | 16 built-in tools: read, write, edit, shell, glob, grep, webfetch, etc. |
| `@belarusian/agents` | Agent service with skills, subagents, and built-in presets |
| `@belarusian/bridge` | Context-aware MoE↔dense conversation bridge |
| `@belarusian/cli` | CLI for running agents standalone or as orchestrator workers |

## Installation

### From source

```bash
pnpm install
pnpm build
```

### As a third-party dependency

Packages are published to GitHub Packages under `@belarusian` scope. Add auth token:

```bash
echo "//npm.pkg.github.com/:_authToken=ghp_YOUR_TOKEN" >> ~/.npmrc
echo "@belarusian:registry=https://npm.pkg.github.com/" >> ~/.npmrc
```

Then install:

```bash
# Just the agent loop
pnpm add @belarusian/harness effect

# Agent loop + tools
pnpm add @belarusian/harness @belarusian/tools effect

# Full stack (agents)
pnpm add @belarusian/agents @belarusian/harness effect
```

## Quick Start

### CLI

```bash
opencode-agent run \
  --prompt "Build a REST API for user auth" \
  --model "qwen3-coder" \
  --url "http://localhost:8080/v1"
```

### SDK

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

## Development

```bash
pnpm install
pnpm build
pnpm test
pnpm typecheck
```

## Testing

```bash
pnpm test  # 635 tests (harness 385 + tools 39 + agents 30 + bridge 181)
```

## License

MIT
