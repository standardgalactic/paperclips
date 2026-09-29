# collective-homelab-stacks

Summary:

The repository "collective-homelab-stacks" focuses on managing and deploying XOA (Xen Orchestra) for controlling xcp-ng hypervisor within a personal/home laboratory environment. XOA is utilized to manage the xcp-ng hypervisor, which serves as the virtualization platform for the homelab. The Docker container for XOA is sourced from a community-maintained repository on Docker Hub, and additional guidance can be found in an associated GitHub project linked in the README.

The primary implementation involves running XOA inside a VM managed by Portainer, another Docker-based tool, which itself runs within xcp-ng. This setup allows for easier management of the hypervisor environment suitable for non-enterprise, personal use cases. For those interested in deeper customization or enterprise-level capabilities, the official installation documentation from Xen Orchestra provides instructions on building XOA from source.

KEYWORDS:
Xen Orchestra
xcp-ng hypervisor
Docker
Portainer
home lab
virtualization management
