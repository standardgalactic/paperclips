# SCC Forth port

The Forth port expresses warrant derivation as a stack transformation. `warrant?` never executes an action; it returns `( flag reason )`. A host execution word may call `EXECUTE` only when `flag` is true. This keeps evidence derivation separate from effectful execution.

`SCC-FORTH-ANS` is the portable semantic profile. `SCC-FORTH-GFORTH` may add file, process, and cryptographic bindings. Neither profile may turn an unavailable verifier into a true flag.
