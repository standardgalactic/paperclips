# microservices

Summary:

SpherePOP is a microservice substrate designed to implement logical grammar through a series of hierarchical processes: POP (Population), REFUSE (Refusal), BIND (Binding), XYLOID (Xyloid Structure), MACROLIFE (Macro Life Cycle), VERIFY (Verification), and COLLAPSE (Collapse). These stages represent core distinctions such as the separation between arrival, admissibility, binding, execution, verification, and commitment, each with distinct operational meanings.

Persistent data is stored across several directories: `data/events/` for events, `data/bindings/` for bindings, `data/candidates/` for candidate states, `data/residuals/` for residuals, and `data/ledger/` for the ledger. The current deployment functions as an architectural skeleton, where each container acts as a real isolation boundary. Protocol handlers can be replaced incrementally with services written in Go, Python, Rust, or other languages without altering the overall topology.

KEYWORDS:
microservice substrate, logical grammar, POP, REFUSE, BIND, XYLOID, MACROLIFE, VERIFY, COLLAPSE, event storage, data directories, isolation boundaries, protocol handlers, replaceable services.
