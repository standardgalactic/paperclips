# carchive

Summary:

The Carchive repository provides test suites for the Carchive application, with a particular emphasis on its agent system functionality. It includes three categories of tests: unit tests covering basic initialization and structure, integration tests interacting with external services like Ollama (specifically requiring `nomic-embed-text`, `llama3.2`, and `llama3.2-vision` models), and end-to-end tests verifying complete workflows. Tests can be executed in various configurations using Poetry's pytest command, allowing for running all tests, specific files or functions, inclusion/exclusion of integration tests via markers, and enhanced verbosity levels for detailed output. Test data is stored in the `tests/test_data/` directory with a default image path set to `tests/test_data/test_image.jpg`. All tests require a functional Python environment along with installed dependencies; integration tests additionally necessitate running Ollama locally with specified models.

KEYWORDS:
Carchive application, agent system, unit tests, integration tests, end-to-end tests, pytest, Poetry, Ollama, nomic-embed-text, llama3.2, llama3.2-vision, test data directory, image path, Python environment, dependencies.
