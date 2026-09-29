# Batch 1

**Centerfuge – 4X Strategy Game Overview**

The *Centerfuge* repository is a prototype implementation of an experimental turn‑based 4X (eXplore, eXpand, eXterminate) strategy game built around the concepts of **entropy economy** and CLI‑driven gameplay. Below are the core features and design principles that define its current state.

---

### Core Gameplay Mechanics

| Feature | Description |
|---------|-------------|
| **Turn Structure** | Players take turns executing a set of commands to manage resources, expand territory, research technologies, and wage war. |
| **Command Syntax** | Use the following verbs in your turn: <br>• `build <factory|lab>` – Construct infrastructure or research facilities.<br>• `scan` – Perform reconnaissance on enemy territories.<br>• `status` – Review current game state (resources, units, techs).<br>• `help` – Display a brief guide to available commands. |
| **Economy & Entropy** | The economy is governed by an *entropy* metric that influences resource scarcity and production costs, encouraging strategic trade-offs between growth and efficiency. |
| **CLI Interface** | All actions are entered via the command line, allowing rapid iteration during development while providing a clear audit trail of each turn’s decisions. |

---

### Technical Status

- **Prototype Phase**: The codebase is still under active development; features may change or be removed as feedback accumulates.
- **No External Dependencies**: Designed to run independently without linking to other projects at this stage, though future versions could integrate with external libraries for AI opponents or enhanced graphics.
- **Documentation**: README includes a brief “help” command and outlines the current limitations (e.g., basic unit movement, simple tech tree).

---

### Design Philosophy

1. **Modular Expansion** – New game elements (units, technologies, terrains) can be added by extending existing modules rather than overhauling core logic.
2. **Scalable Economy** – Entropy as a central mechanic allows for emergent gameplay where resource management becomes increasingly complex with each turn.
3. **CLI Accessibility** – The command‑line interface is intentional to support rapid prototyping and debugging, making it easier for developers to experiment without heavy UI overhead.

---

### Future Directions (Speculative)

- **AI Opponents**: Integration of machine learning agents capable of interpreting `status` outputs to make autonomous decisions.
- **Graphics Enhancements**: Optional rendering modules that visualize the game state graphically while retaining CLI core functionality.
- **Multiplayer Support**: Protocol for networked play, allowing distributed turn management across devices.

---

### Keywords

```
centerfuge
4X strategy game
turn-based gameplay
entropy economy
CLI interface
prototype
```

--- 

This overview captures the essential design intent and current state of the *Centerfuge* project as a proof‑of‑concept for an innovative 4X strategy experience built around economic complexity.
