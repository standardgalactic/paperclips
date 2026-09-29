# test

Summary:

The "test" repository provides a simple Go package designed for testing artifacts against recorded golden files stored in the `testdata/` directory of the caller. It utilizes the [go-cmp](https://github.com/google/go-cmp) package for high-quality diffing. The package includes three main components: 

1. **test.Artifact**: Facilitates testing of artifacts by comparing them to JSON-encoded golden files.
2. **test.File** (deprecated): An older method replaced by `test.Artifact`.
3. **test.Markdown**: Converts code snippets embedded in markdown into executable test cases (`ExampleXXX()` functions). It supports named snippets, importing code from other sources, and special handling for "skip" or "global" snippets to control compilation or scope.

The implementation is currently at a basic level with no advanced features beyond these core functionalities. The repository maintains high standards through integration with Travis CI, GoDoc, Codecov, and Go Report Card for testing and documentation compliance.

KEYWORDS: golang test utils, golden files, go-cmp, markdown tests, code snippets conversion, deprecated file method, skip global handling.
