# Regression fixtures

These artifacts are intentionally versioned.

## source_001

`source_001` is the first end-to-end verified source-card fixture.

It exercises the distinction between:

- model-generated semantic candidates;
- exact source evidence;
- deterministic provenance verification;
- semantic review;
- human adjudication;
- deterministic assembly;
- final verification.

The fixture is not a substitute for the underlying source evidence.

## E000001

`E000001` is a negative encounter regression fixture.

The pipeline retrieved genuinely relevant historical evidence and proposed
an `incompatibility` relation with `warrant_reconstruction_limit`.

That proposal did not survive the warrant chain.

The case is retained to test that the pipeline does not confuse:

- relevance with support;
- information loss with loss of task-required information;
- information loss with reconstruction failure;
- model criticism with independent verification;
- failure to establish a relation with proof of its negation.

A future implementation should continue to prevent this candidate from
becoming a verified positive encounter without new evidence and a new
warrant chain.
