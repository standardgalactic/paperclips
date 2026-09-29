# Mathematical Archaeology Essay Pipeline

A provenance-preserving research-production system for building a large corpus of essays from historical mathematics and a separately curated framework ontology.

The project is designed around a strict separation:

`search formalism != framework formalism != historical evidence`

The essay is not the primary research object. The provenance graph beneath it is.

## Calibration milestone

The first milestone is deliberately small: 20 historical primary sources, approximately 50 curated ontology concepts, roughly 500 candidate encounters, 30 approved specifications, and 10 calibration essays. Sixteen sources are selected from targeted mathematical territories and four from orthogonal territories. Arm identity remains blinded to the encounter pipeline.

## Core invariants

Historical claims must originate in verified, page-addressable primary sources. Modern search vocabulary is never historical attribution. Territory membership and keyword matches are never evidence. Ontology expressions must carry an epistemic status: `native`, `derived`, `candidate_model`, or `encounter_hypothesis`. Encounter hypotheses cannot contribute evidence. No random or model-invented evidence scores are permitted. Unverified historical material cannot become encounter-eligible.

## Initial framework corpus

The scaffold now includes the supplied framework texts under `frameworks/source-texts/` plus a SHA-256 manifest and an initial source-grounded ontology pass. See `docs/FRAMEWORK_SOURCES.md`. Native ontology status means “explicitly present in the framework source,” not “externally verified as true.”

## Quick start

Create a virtual environment and install PyYAML and requests if needed. Then validate the scaffold:

```bash
python scripts/validate_project.py
```

Register a real source only after selecting an actual primary source:

```bash
python scripts/provision_sources.py register source_001 \
  --territory reconstruction_inverse_determination \
  --author "Author" --title "Verified title" --year 1880 \
  --reference "catalogue or archive record"
```

See `docs/METHODOLOGY.md`, `docs/SCHEMAS.md`, `docs/CALIBRATION.md`, and `docs/PIPELINE.md` before running encounter generation.

## Operational boundaries

The pipeline is intentionally split into authority layers. Search territories retrieve candidates; they do not establish historical meaning. Source cards establish what a historical artifact says; they contain no modern interpretation. The ontology establishes what the framework corpus says and records whether each formalization is native, derived, a candidate model, or an encounter hypothesis. Encounter records ask whether independently warranted structures correspond. Claim ledgers make the dependencies of final prose explicit.

The expected workflow is therefore:

```text
territory -> discovered source -> acquired artifact -> verified source card
          -> candidate encounter -> adversarial adjudication -> bounded packet
          -> claim-ledger draft -> audit -> final essay -> corpus index
```

A failure at an earlier stage is not repaired by a later stage. Missing evidence remains missing evidence.

## Useful commands

```bash
python scripts/validate_project.py
python scripts/provision_sources.py status source_001
python scripts/audit_claim_ledger.py packets/E000001/claim-ledger.yaml
```

See `docs/LIFECYCLE.md`, `docs/BLINDING.md`, `docs/CLAIM_LEDGER.md`, and `docs/EXPERIMENT.md` for the expanded operational specification.

## v0.4: first evidence-bearing run

The repository now contains its first acquired primary-source artifact, `source_001`, a user-supplied scan of P. Cousot's 1972 AFCET paper. The original is content-addressed by SHA-256 and remains intentionally stopped at the `acquired` lifecycle state. No OCR/transcription, historical claim, or framework correspondence has been promoted to verified evidence.

`audit_claim_ledger.py` now performs referential resolution rather than token-shape checking. See `docs/REFERENTIAL_INTEGRITY.md`.

## v0.4.3: Cousot extraction checkpoint

`source_001` is now at `extraction_initialized`. Required article pages 391–394 (scan pages 2–5) have manual transcription artifacts; pages 391–392 are verified and pages 393–394 remain extracted but unverified. Source-level `text_extracted` and `text_verified` remain false until their respective all-required-page gates are satisfied.

### v0.4.4 checkpoint
Scan page 6 / printed page 395 added as an unverified manual transcription. Source progress: 5/15 required pages extracted, 2/15 verified.
