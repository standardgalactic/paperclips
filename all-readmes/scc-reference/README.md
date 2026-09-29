# Scope-Carrying Certificate Reference Runtime

This repository is a minimal executable reference implementation of Scope-Carrying Certificates (SCCs). It separates static factorization evidence from runtime domain membership and requires explicit evidence for downstream composition.

The authorization rule is conceptually:

`trusted factorization proof AND current history in admitted domain AND valid live assumptions AND valid composition evidence => warrant`

A missing warrant is not classified as proof that an action is unsafe. The runtime instead refuses to invoke the sink and returns `NULL_ACTION` where additional evidence, sensing, or renewal may make progress possible.

## Layout

- `scc_runtime/models.py` — SCC, proof, composition, history, and result models.
- `scc_runtime/registry.py` — trusted proof/composition registry plus domain semantics.
- `scc_runtime/engine.py` — three-gate enforcement and non-transitive delegation.
- `scc_runtime/legacy.py` — deliberately naive Boolean runtime used as the counterexample.
- `demo.py` — executable seven-row matrix plus the legacy violation.
- `tests/test_runtime.py` — pytest regression suite.
- `neuroformal/` — property-relative translation certificates, bridge/terminal proof registries, and representational warrant enforcement.
- `tests/test_neuroformal.py` — counterexamples and controls for semantic loss across translation.
- `docs/unified-calculus.md` — the generalized temporal/structural/representational preservation law.

## Run

```bash
python -m pip install -r requirements.txt
python demo.py
pytest -q
```

The demonstration covers: invalid factorization evidence, valid root execution, domain escape, missing composition evidence, environmental drift, stale certificates, and a fully certified delegated chain.

## Important design properties

Identifiers used in authorization are semantic hashes rather than human-readable labels. Domain membership is evaluated through registry-bound predicates. Environmental evidence fails closed. Delegation does not inherit `PROCEED` transitively. Composition requires a registry-backed evidence object rather than a caller-provided `True` flag.

This is a reference model, not a production cryptographic verifier. A production implementation would replace the in-memory registry and illustrative hash strings with authenticated artifacts, canonical serialization, signature verification, durable provenance, revocation/version policy, and an actual proof checker or proof-carrying artifact pipeline.


## Unified calculus

The repository treats temporal truncation, workflow projection, and source-to-formal translation as instances of the same transformation problem. A warrant may cross an information-losing map only when independently verifiable evidence establishes that the relevant property is invariant over the map's fibers on the admitted domain. See `docs/unified-calculus.md`.


## Manual pages

The repository includes traditional Unix-style manual pages under `man/`: section 1 documents executable demonstrations, section 3 documents library functions and methods, section 5 documents certificate/evidence formats, and section 7 documents the unified warrant calculus. Read a page directly with `man -l man/man7/scc-warrant-calculus.7` or consult `docs/api.md` for the browsable API manual. Public and internal callables are documented in source docstrings as well.


## Unix command suite

Version 0.2.0 adds Unix-style wrappers installed by `pip install -e .`: `scc`, `scc-hash`, `scc-check`, `scc-inspect`, `scc-explain`, `scc-trace`, `scc-verify-chain`, `scc-fiber`, `scc-translate`, `scc-prove`, `scc-seal-decision`, and `scc-run`. The same operations are available as `scc <subcommand>`.

`scc-fiber` operationalizes the central preservation criterion over finite JSON test sets. `scc-run` is the execution boundary: it refuses unauthenticated or non-PROCEED decision records and invokes the requested program with `shell=False`. Decision records can be authenticated with `scc-seal-decision` using a key controlled by the trusted runtime/operator boundary. This HMAC mechanism is a reference transport binding, not a replacement for a production key-management or signature system.

Example fiber input is a JSON array whose rows contain `T` and `Phi` fields. If two rows have equal `T` values but unequal `Phi` values, `scc-fiber` emits the witness and exits 77.

```sh
printf '%s\n' '[{"T":"external","Phi":true},{"T":"external","Phi":false}]' > /tmp/fibers.json
scc-fiber /tmp/fibers.json
```

For local manual pages, use for example `man -l man/man1/scc-fiber.1` or `man -l man/man1/scc-run.1`.

## Asynchronous orchestration

The `orchestration/` package places an actual asynchronous execution boundary behind SCC warrant derivation. It includes `SCCMiddleware`, a minimal `ReferenceOrchestrator`, explicit delegation and join records, an append-only provenance ledger, concurrent governed jobs, and a `NULL_ACTION` evidence-reacquisition path. See `docs/orchestration.md`.


## Research Unix layer (0.4.0)

The repository now includes normative `spec/` documents, a relocatable `etc/scc` and `var` hierarchy, SCC/1.0 interchange fixtures, and classic diagnostic utilities: `scc-fsck`, `scc-lint`, `scc-dump`, `scc-od`, `scc-tail`, and `scc-replay`. Set `SCC_ROOT` to relocate the subsystem. See `docs/research-unix.md`, `docs/rationale.md`, `scc-paths(7)`, and `scc-protocol(5)`.

## XENIX personality (0.4.1)

Release 0.4.1 adds an explicitly fictional alternate-history XENIX/386 presentation layer. It does **not** claim derivation from, inclusion of, or binary compatibility with Microsoft XENIX. `SCC_XENIX=1` selects the period presentation; `SCC_ROOT` keeps the emulated `/etc`, `/var/lib`, `/var/log`, and spool hierarchy relocatable. Administrative commands are `sccinit`, `sccstat`, `sccadm`, and `scclog`. See `docs/xenix-personality.md` and `scc-xenix(8)`.


## Portable Kernel (0.4.2)

Release 0.4.2 adds deliberately constrained BASIC and Forth ports under `ports/`, plus shared cross-language conformance vectors. The ports separate seven semantic operations—canonicalize, hash, resolve, domain check, ancestry check, derive, and audit—from host-specific cryptography and execution. `SCC-BASIC-16`/`32` and `SCC-FORTH-ANS`/`GFORTH` are modern portability profiles, not historical claims. See `docs/porting-guide.md`, `sccport(7)`, `sccbasic(7)`, and `sccforth(7)`.
