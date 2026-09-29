# @belarusian/bridge

Context-aware conversation bridge between two LLM servers for multi-stage reasoning workflows.

## Overview

The bridge module extends `@belarusian/harness` with a multiplexer that manages two concurrent LLM sessions (MoE + dense) and handles context handoff between them.

### Architecture

```
User Terminal
     │
     ▼
  Bridge
     │
     ├─► Explorer Session (MoE) ──► LLM Client
     │                              (llama.cpp:8080)
     │
     └─► Producer Session (Dense) ─► LLM Client
                                   (llama.cpp:8081)
```

### Workflow

1. **Brainstorm on MoE** - Fast server with large context window. Explore codebase, iterate directions cheaply.
2. **Trigger "go deep"** - User-initiated command pushes selected context to the dense session.
3. **Implement on dense** - Higher-quality output with deeper reasoning per token.
4. **Stream results back** - Dense output feeds into MoE session.

## Installation

```bash
npm install @belarusian/bridge
```

## Usage

### Basic Example

```typescript
import { bridgeCLI } from "@belarusian/bridge"
import { Effect } from "effect"

// Run the CLI
Effect.runPromise(bridgeCLI)
```

### Programmatic Usage

```typescript
import { startBridge, runTurn, transferContext } from "@belarusian/bridge"
import { Message } from "@belarusian/harness"

const config = {
  explorer: {
    url: "http://localhost:8080",
    model: "qwen3.6-35b-a3b",
    role: "explorer",
  },
  producer: {
    url: "http://localhost:8081",
    model: "qwen3.6-27b",
    role: "producer",
  },
}

const bridge = await startBridge(config, "~/.cache/bridge").pipe(
  Effect.runPromise,
)

const userMsg = Message.user("Let's design a REST API")

const update = await runTurn(bridge.explorerSession, userMsg).pipe(
  Effect.runPromise,
)

// Transfer to dense session
const denseMessages = await transferContext(
  bridge.explorerSession,
  bridge.producerSession,
  { turns: 5 },
).pipe(Effect.runPromise)
```

### CLI Commands

```bash
# Start interactive mode
bridge start \
  --explorer http://localhost:8080 \
  --producer http://localhost:8081

# Batch context transfer
bridge deep \
  --from explorer \
  --to producer \
  --turns 10

# Check session status
bridge status

# View conversation history
bridge history --session explorer
```

## API Reference

### Types

- `BridgeConfig` - Configuration for the two sessions
- `BridgeSession` - State for a single session
- `Bridge` - The full bridge state
- `Lineage` - Origin tracking metadata
- `TransferOptions` - Options for context transfer

### Core Functions

- `startBridge(config, stateDir)` - Initialize bridge with two sessions
- `runTurn(session, userMessage)` - Execute a single turn
- `transferContext(from, to, options)` - Transfer context between sessions
- `mergeBack(explorer, denseMessages)` - Merge dense output into explorer
- `saveState(bridge)` - Persist bridge state to disk
- `loadState(stateDir)` - Restore bridge state from disk

### Utility Functions

- `annotateWithLineage(messages, session)` - Attach origin metadata
- `getLineage(message)` - Extract lineage from message
- `filterByOrigin(messages, origin)` - Filter by model/server
- `traceHistory(messageID, session)` - Trace message history
- `selectTurns(messages, range)` - Select specific turns
- `filterByRole(messages, roles)` - Filter by role

## Testing

```bash
# Run all tests
bun test

# Run specific test file
bun test test/lineage.test.ts
```

## License

MIT
