# CPR-OS Prototype

A small userspace prototype for an operating-system style environment based on Spherepop, CLIO, MEM|8, and RSVP/CPR.

This is not a kernel. It is a minimal shell/runtime showing how the principles could become executable.

## Quick start

```bash
python3 cprsh.py init
python3 cprsh.py pop examples/sample.txt
python3 cprsh.py collapse examples/sample.txt
python3 cprsh.py refuse examples/sample_summary.txt examples/sample.txt
python3 cprsh.py graph examples/tasks.json
python3 cprsh.py health examples/tasks.json
bash demo.sh
```

## Principles

Most systems treat files, processes, and states as primitive. This prototype treats events and transformations as primitive:

```text
history -> projection -> state
```

Spherepop operations are modeled as event-generating transformations:

```text
pop       extract distinctions
collapse  make a lossy projection
refuse    reject a projection that loses distinctions
bind      preserve provenance across combined artifacts
repair    restore reachability
```
