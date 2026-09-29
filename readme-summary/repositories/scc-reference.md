# scc-reference

Summary:

The scc-reference repository provides conformance vectors designed to test the portable three-gate kernel. It includes two CSV files: `decisions.csv`, which exercises core functionality, and `fibers.csv`, containing a counterexample due to differing property values for observations mapped to `external`. A conforming port must correctly process each decision row, reporting a fiber violation for any entry labeled `external`. The focus is on conformance testing rather than cryptographic security.

KEYWORDS: scc-reference, conformance vectors, three-gate kernel, decisions.csv, fibers.csv, external mapping, fiber violation, non-cryptographic testing.
