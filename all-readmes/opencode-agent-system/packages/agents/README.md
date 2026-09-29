# @belarusian/agents

Agent service, skills, and subagent spawning for multi-agent workflows. Part of the [@belarusian](https://github.com/belarusian) ecosystem.

## Overview

This package provides the orchestration layer for agent-based workflows:

| Module | Description |
|---|---|
| `Agent` | Agent service — manages agent lifecycle, profile resolution, and execution context |
| `Skill` | Skill system — YAML-based skill definitions with validation, loading, and hot-reload |
| `Subagent` | Subagent spawning — fork agent processes with isolated context and resource limits |

## Architecture

```
@belarusian/agents (this package)
├── Agent      → service layer: profile matching, state management
├── Skill      → skill definitions loaded from YAML config
└── Subagent   → process spawning with IPC communication

Dependencies:
├── @belarusian/harness → LLM client + agent loop (runAgent, streamAgent)
├── @belarusian/tools   → tool definitions for file/shell/search operations
└── effect              → Effect-TS runtime
```

## Usage

```ts
import { Agent, Skill, Subagent } from "@belarusian/agents";

// Create an agent with a profile and LLM endpoint
const agent = Agent.makeAgent({
  profile: "dev",
  model: "qwen3-coder",
  baseUrl: "http://localhost:8080/v1",
});

// Load skills from YAML config
const skills = Skill.loadSkills("./skills/");

// Spawn a subagent with isolated context
const child = Subagent.spawn({
  command: "npx opencode-agent-system run",
  timeoutMs: 300_000,
  env: { AGENT_PROFILE: "implementer" },
});
```

## Dependencies

- `@belarusian/harness` — LLM client for agent execution
- `@belarusian/tools` — tool definitions used by agents
- `effect` — Effect-TS runtime
- `gray-matter` — YAML frontmatter parsing for skill definitions

## Build

```bash
pnpm build   # tsc → dist/
pnpm test    # vitest (30 tests pass)
```
