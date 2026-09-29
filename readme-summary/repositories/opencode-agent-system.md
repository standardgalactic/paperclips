# opencode-agent-system

**Summary**

The *opencode-agent-system* repository hosts a collection of utility functions (`@belarusian/tools`) designed to support workflow agents within the broader **@belarusian** ecosystem. These tools provide low‑level I/O operations (reading/writing files, editing text with context checks), shell execution with timeout safety, pattern matching via globbing and regex search, HTTP‑based web searches and fetches, Git repository cloning and structural overviews, file truncation helpers, patch application, task management (`todo`), and an interactive question prompt. All tools are defined to be compatible with the `@belarusian/harness`, leveraging its execution context types (e.g., `ToolExecuteContext`) and effect handling via `effect` utilities.

The package is intentionally lightweight—only a set of primitive operations needed for building more complex agent workflows—and currently **incomplete**; it lacks advanced features such as multi‑step orchestration or integration with higher‑level AI agents beyond the basic harness compatibility. The implementation status reflects an early prototype stage, intended to be extended by downstream projects that require reliable I/O and shell execution primitives.

**KEYWORDS:** tools, utilities, agent workflows, @belarusian ecosystem, file I/O, shell execution, glob patterns, HTTP fetches, Git cloning, task management, incomplete prototype.
