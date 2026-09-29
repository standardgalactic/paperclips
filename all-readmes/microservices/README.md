# microservices

An experimental Docker microservice substrate that expresses a small protocol grammar as real service boundaries.

```text
external input
      |
      v
    POP
      |
      v
   REFUSE
      |
      v
    BIND
      |
  +---+---+
  |       |
  v       v
XYLOID  MACROLIFE
  |       |
  +---+---+
      |
      v
   VERIFY
      |
      v
  COLLAPSE
      |
      v
   LEDGER
```

The architecture keeps several distinctions explicit:

```text
arrival       != admissibility
admissibility != binding
binding       != execution
execution     != verification
verification  != commitment
commitment    != history
```

POP establishes event identity and binds the payload hash at ingress.

REFUSE is an explicit admissibility boundary rather than a generic error path.

BIND records the relation between an event, its context, and the operation that may act upon it.

Transform services produce candidate outputs but do not certify themselves.

VERIFY independently re-derives the properties required for acceptance.

COLLAPSE commits an already verified outcome.

The ledger preserves the resulting history monotonically, including refusals and residuals.

## Event identity

```text
payload_hash = sha256(canonical_payload)
event_id     = sha256(source | payload_hash)[:16]
```

For structured inline JSON, the payload is canonicalized before hashing so insignificant serialization differences do not change identity.

## Development

Deploy the live topology:

```bash
./deploy-spherepop-live.sh
```

Run the sample:

```bash
./test-spherepop.sh
```

Inspect services:

```bash
docker compose ps
docker compose logs -f
```
