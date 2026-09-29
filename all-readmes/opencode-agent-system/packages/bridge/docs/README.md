# Bridge Documentation Hub

Complete documentation for the `@belarusian/bridge` package.

## Getting Started
- [CLI Guide](cli-guide.md) — Interactive terminal usage, commands, configuration
- [API Reference](api-reference.md) — All functions with signatures and descriptions
- [Deployment Guide](deployment-guide.md) — Standalone vs monorepo setup

## Architecture
- [Context Transfer Strategies](context-transfer-strategies.md) — messages vs slot-save comparison
- [Lineage Guide](lineage-guide.md) — Origin tracking and query API
- [Harness Bridge Architecture](../harness/docs/bridge-architecture.md) — A* search vs standalone multiplexer
- [Harness Bridge Quickstart](../harness/docs/bridge-quickstart.md) — runAgent() bridge config

## Examples
- [basic.ts](../examples/basic.ts) — Full lifecycle: start → explore → yield → produce → mergeBack
- [cli-basic.ts](../examples/cli-basic.ts) — Programmatic CLI usage
- [cli-interactive.ts](../examples/cli-interactive.ts) — Interactive session simulation

## Testing
All test files are in the `test/` directory:
- Unit tests: `mux.test.ts`, `lineage.test.ts`, `context-transfer.test.ts`, `bridge-cli.test.ts`
- Integration tests: `integration.test.ts`, `mux-integration.test.ts`, `lifecycle-integration.test.ts`
- CLI tests: `cli-parser.test.ts`, `cli-input.test.ts`, `cli-commands.test.ts`, `cli-health.test.ts`, `cli-history.test.ts`, `cli-state.test.ts`, `cli-lineage.test.ts`, `cli-slots.test.ts`, `cli-config-loader.test.ts`
- Edge cases: `mux-edge-cases.test.ts`, `api-surface.test.ts`

## Running Tests

```bash
# All bridge tests (unit + integration)
npx vitest run

# Unit tests only (no server needed)
npx vitest run test/mux.test.ts test/lineage.test.ts test/context-transfer.test.ts \
  test/bridge-cli.test.ts test/cli-parser.test.ts test/cli-input.test.ts \
  test/cli-commands.test.ts test/cli-health.test.ts test/cli-history.test.ts \
  test/cli-state.test.ts test/cli-lineage.test.ts test/cli-slots.test.ts \
  test/cli-config-loader.test.ts test/api-surface.test.ts

# Integration tests (requires llama.cpp at localhost:8080)
npx vitest run test/mux-integration.test.ts test/context-transfer-integration.test.ts \
  test/lineage-integration.test.ts test/lifecycle-integration.test.ts \
  test/integration.test.ts
```
