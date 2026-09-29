# Portable conformance vectors

These fixtures are deliberately representationally primitive. `decisions.csv` exercises the portable three-gate kernel; `fibers.csv` contains a finite counterexample to warrant preservation because two observations map to `external` while their property values differ.

A conforming port MUST produce the expected disposition/reason pair for every decision row and MUST report a fiber violation for `external`. The vectors test the calculus, not cryptographic strength.
