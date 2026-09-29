# nixos-config

**Summary**

The *nixos-config* repository is a modular configuration framework for NixOS and Nix-Darwin systems, inspired by several existing projects (e.g., MatthiasBenaets/nixos-config, cors/nixos-config). It aims to provide shared, reusable modules (`lib/mkSystem.nix`) that can be applied across different configurations, facilitating a more organized and maintainable setup for both NixOS and Nix-Darwin environments.

Key features include:

- **Shared Modules**: Encapsulates common configuration patterns into reusable parts.
- **Flake Support**: Utilizes flakes to manage dependencies and state changes (`nix flake update`).
- **Command-Line Utilities**: Provides scripts like `darwin-rebuild switch --flake` for quick system updates on macOS/NixOS, and `nix build '.#fgnix'` for building/testing the configuration.
- **Testing Infrastructure**: Includes automated test execution via `nix build '.#fgnix'`, as well as interactive debugging tools (`nixos-test-driver`) to facilitate troubleshooting of individual components.

The repository is designed to be compatible with various installation guides (e.g., NixOS manual, Home-manager documentation) and supports both NixOS and Nix-Darwin setups. It emphasizes modularity, maintainability, and ease of updates through flake mechanisms.

**KEYWORDS:**
nixos-config
configuration framework
NixOS
Nix-Darwin
shared modules
flakes
rebuild commands
testing infrastructure
modularization
