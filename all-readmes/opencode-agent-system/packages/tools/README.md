# @belarusian/tools

File I/O, shell execution, search, and HTTP tools for agent workflows. Part of the [@belarusian](https://github.com/belarusian) ecosystem.

## Overview

This package provides a collection of ready-to-use tool definitions compatible with `@belarusian/harness`:

| Tool | Description |
|---|---|
| `read` | Read files and directories with line/offset support |
| `write` | Create or overwrite files (atomic — writes to temp then moves) |
| `edit` | Replace exact text in files with context verification |
| `shell` | Execute shell commands with timeout protection |
| `glob` | Glob pattern file matching with size limits |
| `grep` | Search file contents by regex or literal text |
| `websearch` | Launch a web search (via configured provider) |
| `webfetch` | Fetch a URL as text or markdown |
| `repoClone` | Clone a Git repository to the working directory |
| `repoOverview` | Summarize a repository's structure without cloning |
| `truncate` | Truncate file to N lines from start/end/middle |
| `applyPatch` | Apply diff/patch text to existing files |
| `todo` | Manage a structured task list with pending/in_progress/completed states |
| `question` | Interactive question tool — prompt user for input |
| `lsp` | LSP diagnostics and references (LSP-aware operations) |

## Usage

```ts
import { read, write, shell } from "@belarusian/tools";

// Tools are plain objects compatible with @belarusian/harness tool definitions
console.log(read.name); // "read"
console.log(read.parameters); // JSON Schema for the tool's input params
```

## Dependencies

- `@belarusian/harness` — for `ToolExecuteContext` type (re-exported)
- `effect` — Effect types used in tool execution context
- `execa` — shell command execution
- `fast-glob` — glob pattern matching

## Build

```bash
pnpm build   # tsc → dist/
pnpm test    # vitest
```
