# Batch 10

**Key Components**

- **Triage Agents**
  - `triage_assessor` – analyzes incoming issues and pull requests.
  - `pr_reviewer` – reviews code quality and detects breaking changes.

- **Ecosystem Agents**
  - `dependency_tracker` – maintains a cross‑repo dependency graph.
  - `sync_coordinator` – ensures consistent repository configuration across the fleet.

- **Planning Agents**
  - `sprint_planner` – organizes weekly sprints.
  - `roadmap_curator` – updates quarterly roadmaps.

These agents are invoked via the `agentic-control` CLI (e.g., `npx agentic-control triage assess <issue-number>`), and their behavior is defined in YAML configuration files (`config/agents.yaml`, `config/tasks.yaml`). Integration with GitHub Actions workflows (`agentic-triage.yml`, `triage.yml`, `ecosystem-sync.yml`) automates the execution of these agents.

**Dependencies Required**

- Core control framework: `agentic-control`.
- Triaging utilities: `agentic-triage`.
- CrewAI execution layer for Python crews: `agentic-crew`.

**Open Issues Affecting Maturity**

- jbcom/agentic‑control#22 – adding `triage_assessor` as a dependency.
- jbcom/agentic‑control#28 – monitoring npm releases.
- jbcom/agentic‑control#29 – improving fleet agent spawning.

**KEYWORDS:** control center, CrewAI, agentic-control, triage agents, ecosystem agents, planning agents, configuration files, GitHub Actions, dependencies, open issues.
