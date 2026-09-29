# echoes-of-beastlight

**Summary**

The *echoes-of-beastlight* repository contains a comprehensive **AI Game Generator Test Suite** designed to validate the functionality, reliability, and robustness of an AI-driven game generation system. The suite includes:

- **Unit tests** for individual modules (config parsing/validation, template rendering, generator logic, Git tracker operations) ensuring >80% coverage of core logic.
- **Integration tests** covering end‑to‑end workflows such as OpenAI API interactions and full game generation pipelines, including error scenarios like missing/invalid configurations.
- **Property‑based tests** using `proptest` to verify deterministic behavior across arbitrary inputs (game titles, cache keys, file paths).
- A well‑structured test organization (`tests/unit`, `tests/integration`, `tests/fixtures`) with explicit commands for running all or specific subsets of tests.

The repository leverages mocking tools like **WireMock** and **Tempfile** to isolate external dependencies and ensure clean, reproducible environments. It also defines clear coverage goals (unit >80%, integration 100%) and provides templates for writing new tests, facilitating maintainability and scalability within a larger game development ecosystem.

**KEYWORDS:**
ai game generator test suite, unit testing, integration testing, property-based testing, mock server, tempfile isolation, coverage metrics, openai api integration, deterministic behavior.
