SpherePOP microservice substrate
================================

Logical grammar:

    POP
     |
    REFUSE
     |
    BIND
     |
     +--------------+
     |              |
   XYLOID       MACROLIFE
     |              |
     +-------+------+
             |
           VERIFY
             |
          COLLAPSE
             |
           LEDGER


Core distinctions:

    arrival       != admissibility
    admissibility != binding
    binding       != execution
    execution     != verification
    verification  != commitment
    commitment    != history


Persistent data:

    data/events/
    data/bindings/
    data/candidates/
    data/residuals/
    data/ledger/


The current deployment is an architectural skeleton.

Each container represents a real isolation boundary, but the protocol
handlers themselves can now be replaced one by one with small Go,
Python, Rust, or other services without changing the topology.
