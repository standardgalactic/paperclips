# CPR-OS Prototype v0.2

A userspace prototype for an operating-system style environment based on
Spherepop, CLIO, MEM|8, and RSVP/CPR.

This is not a kernel. It is a minimal shell/runtime showing how the principles
can become executable.

## Quick start

```bash
python3 cprsh.py init
bash demo.sh
```

## What changed in v0.2

**Histories are first-class objects** (MEM|8 becomes operational, not metaphorical)

Instead of `report.txt`, the system stores `report.history` — a Merkle chain
of events, each with provenance hash, parent pointer, and distinction budget:

```
history → projection → state
```

**New commands:**

```
record HISTORY --op OP [--text TEXT | --file FILE]
    append an event to a .history file

state HISTORY [--raw]
    reconstruct the current artifact from history
    (uses stored payload, not recomputation)

trace HISTORY
    print the full event chain
    the chain IS the program — execution is replay

fiber HISTORY
    find alternative histories that reach the same terminal artifact
    same residue, different trajectories
    direct implementation of Chapter 1
```

**Distinction budgets on every event:**

Every `record`, `collapse`, and `refuse` now reports:

```json
{
  "distinctions_before": 3,
  "distinctions_after": 1,
  "loss": 2
}
```

**Collapse with budget enforcement:**

```bash
python3 cprsh.py collapse paper.txt --max-loss 5
```

Refuses if the projection would lose more than 5 distinctions.
This is the CLIO constraint made executable.

**Composable refuse (Unix filter):**

```bash
cat paper.txt | python3 cprsh.py collapse - --top 5 | python3 cprsh.py refuse - --against paper.txt
```

If refusal occurs, exit 2 halts the pipeline.
Refusal is now a first-class execution primitive.

**Fixed graph example:**

`resubmit` is now only reachable through the blocked edge, so repair
visibly expands reachability: health goes from 0.875 → 1.0.

## History format (Merkle chain)

Each line in a `.history` file is a JSON event:

```json
{"op":"create",  "hash":"<sha256>", "parent":null,   "payload":"...",
 "distinctions_before":0, "distinctions_after":3, "loss":0, "time":...}
{"op":"summarize","hash":"<sha256>", "parent":"<prev>","payload":"...",
 "distinctions_before":3,"distinctions_after":1,"loss":2,"time":...}
```

Reconstruction uses the **stored payload**, not recomputation.
This means histories survive changes to the operations that produced them.
Verification reruns the operation and checks that the stored hash matches.

## The architecture

Most systems are:
```
state-first
history-second
```

This prototype is:
```
history-first
state-derived
```

The distinction is not cosmetic. When execution is replay, the difference
between "running a program" and "reading its history" disappears. Refusals,
collapses, and distinction budgets are not annotations on computation —
they are the computation.

## Spherepop operations

```
pop       extract distinctions from an artifact
collapse  make a lossy projection (reports what is lost)
refuse    reject a projection that loses reachability-relevant distinctions
bind      preserve provenance across combined artifacts
repair    restore reachability by removing blocked edges
record    append a named operation to a history chain
state     reconstruct current artifact from history
trace     read the program (the chain is the program)
fiber     find alternative histories to the same artifact
```
