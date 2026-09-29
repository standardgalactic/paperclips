# ws-skilstak

Summary:

The ws-skilstak repository provides a quick-start container image for learning Linux and containers, primarily targeting users who wish to keep up with live streaming content or need an immediate setup of Linux on their local machine. It includes instructions for installing terminal software (iTerm2 for Mac, git-bash for Windows), bash, and Podman Desktop. Users are guided through initializing and starting a Podman virtual machine using specific commands (`podman machine init` and `podman machine start`). A container is then created from the SKILSTAK workspace image with the command `podman run -it --hostname skilstak --name skilstak -v shared://shared ghcr.io/rwxrob/ws-skilstak`. Exiting the container is managed via the `exit` command, and restarting it can be done using `podman start -a skilstak`.

KEYWORDS:
ws-skilstak repository, Linux learning, containers, quick start, Podman, bash installation, iTerm2, git-bash, virtual machine setup, container image.
