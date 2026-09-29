# SCC BASIC port

This directory demonstrates the SCC Portable Kernel in intentionally constrained BASIC. `SCC.BAS` contains the authorization state machine; `CERT.BAS` gives a fixed-width record view; `STORE.BAS` documents the external-crypto rule; `TEST.BAS` is a five-case smoke test.

The source is written in a conservative QBasic/FreeBASIC-like dialect, but dialects differ. `SCC-BASIC-16` is the constrained profile: it MAY use flat files and an external trusted SHA-256/signature verifier, and it MUST NOT claim cryptographic verification when that primitive is unavailable. `SCC-BASIC-32` may provide those primitives natively. The authorization semantics are identical.
