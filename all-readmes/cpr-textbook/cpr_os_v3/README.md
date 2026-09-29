# cprsh — history-native runtime (v0.3)

A userspace runtime where histories, refusals, distinction ledgers, and
reachability are primitive objects — not annotations on a state-first system.

```
history (event DAG)
    ↓  record / branch / merge
projection (collapse / pop)
    ↓  distinction ledger
state (reconstruction)
    ↓  reach
reachability (future set)
    ↓  admissibility policy
constraint (refuse / continue)
```

## Quick start

```bash
python3 cprsh.py init
bash demo.sh
```

## What's new in v0.3

### Event DAGs (not just chains)

Histories branch and merge. `parents` is a list:

```
[]        = root commit
["hash"]  = linear step
["a","b"] = merge commit
```

```bash
cprsh branch report examples/report_branch --from-hash 24326bcf
cprsh record examples/report_branch --op translate --text "..."
cprsh merge report examples/report_branch --payload "..."
```

### Distinction ledgers

Every event stores the full distinction delta as named sets, not scalars:

```json
"ledger": {
  "preserved": ["memory is not storage."],
  "lost":      ["a label is not a trajectory."],
  "gained":    [],
  "loss": 1, "gain": 0,
  "count_before": 3, "count_after": 2
}
```

The ledger is the accounting layer for CLIO constraints.

### Reachability as a first-class runtime object

```bash
cprsh reach report
```

Output:
```json
{
  "available_futures": [{"op": "edit", "hash": "25ee6b08…"}],
  "blocked_futures":   [],
  "continuation_hints": ["archive", "publish", "revise"],
  "reachability_score": 1.0
}
```

Blocked futures are **Refuse events in the history** — trajectories that were
attempted and rejected. The distinction is preserved; the reachability is not.

### Admissibility policies

Place a `.policy` file alongside a `.history` file to constrain operations:

```json
{
  "max_loss": 1,
  "must_preserve": ["memory is not storage"],
  "denied_ops": ["delete"]
}
```

Policy violations are recorded as **first-class Refuse events** in the
history chain — not silent failures. The history still contains the attempt.

### Verify

```bash
cprsh verify report
```

Replays the chain and checks:
1. `sha256(payload) == stored hash`
2. Parent hashes exist (cross-history refs noted as warnings, not errors)
3. Distinction ledger is consistent with stored vs parent payload

### Semantic diff

```bash
cprsh sdiff file_a.txt file_b.txt
```

Emits the full distinction ledger between two texts — what was gained, lost,
and preserved. More informative than line-level diff for prose documents.

### Suggest-repair

```bash
cprsh suggest-repair graph.json
```

Enumerates repair candidates ordered by reachability gain, without
automatically applying any of them. Repair becomes search.

### Trace (DAG-aware)

```bash
cprsh trace report
```

Each event is typed: `root`, `linear`, `merge`, or `refuse`.
The trace IS the program — execution is replay.

## All commands

```
# file operations
pop FILE              extract distinctions from text
collapse FILE         lossy word-frequency projection + ledger
sdiff A B             semantic diff: gained/lost/preserved distinctions
refuse [PROJ ORIG]    check or enforce distinction preservation
  --against FILE      original file (pipeline mode)

# graph reachability
graph FILE            reachability before/after repair
health FILE           reachability ratio
repair FILE           restore reachability (writes new file)
suggest-repair FILE   enumerate repair candidates with gain estimates
bind LEFT RIGHT       bind two files preserving provenance

# history
record HIST --op OP   append event (respects .policy if present)
branch SRC DEST       fork history at a commit
merge TARGET SRC      merge two histories
state HIST            reconstruct current artifact
trace HIST            print the event DAG
fiber HIST            find alternative histories to same artifact
reach HIST            reachability as runtime object
verify HIST           replay and validate the chain
log [--tail N]        show event log
```

## History format

```
.history    JSONL event DAG (one entry per line)
.policy     JSON admissibility constraints (optional, loaded on record)
```

Each history entry:
```json
{
  "op":      "edit",
  "hash":    "<sha256 of payload>",
  "parents": ["<parent hash>"],
  "payload": "...",
  "ledger":  {"preserved":[], "lost":[], "gained":[], "loss":0, "gain":0},
  "time":    1234567890.0
}
```

## What this is not

This is not a kernel, a process scheduler, or a replacement for a filesystem.
It is a research prototype demonstrating that a system can be organized around
the ontological primitives developed in the CPR manuscript:

- history is primary; state is derived
- refusal is execution, not error handling
- distinction loss is measurable and constrainable
- fibers (π⁻¹(artifact)) are first-class objects
- reachability is a runtime metric, not a graph-theory concept applied post hoc
