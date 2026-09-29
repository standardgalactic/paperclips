# firecracker-arch

SUMMARY:

The firecracker-arch repository aims to enable rapid provisioning of virtual machines (VMs) on a home network, potentially accessible externally via Tailscale, running Arch Linux with the user's dotfiles. It targets solving the hassle of maintaining consistent configurations across multiple machines by allowing seamless VM setup and integration with tools like UpspinFS for persistent `$HOME` mounting.

Key components include:

- **Firecracker MicroVM**: The underlying virtualization engine used to run lightweight VMs.
- **Arch Linux Root Filesystem**: A custom root filesystem script (`create-arch-rootfs.sh`) generates a minimal Arch Linux environment.
- **Kernel Setup**: Utilizes the `vmlinux` target from the Linux kernel source for proper kernel configuration.
- **Network Configuration**: Guides for setting up bridge network interfaces on the host machine, crucial for Tailscale integration.
- **VM Launch Script**: The `02-launch_vm.sh` script automates VM creation with a specified alias (e.g., `foobar`).

The project is currently in an experimental phase, focusing on proof-of-concept functionality rather than full production readiness. It leverages existing tools like Tailscale for network connectivity and UpspinFS for persistent home directory synchronization.

KEYWORDS:
firecracker microvm
Arch Linux
dotfiles
Tailscale
UpspinFS
root filesystem
VM launch script
