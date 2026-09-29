# NeurobloxRegistry

Summary:

The NeurobloxRegistry is a Julia package registry designed to facilitate easy installation of the Neuroblox.jl library within the Julia programming environment. It functions as an additional registry that can be added using the command `pkg"registry add https://github.com/Neuroblox/NeurobloxRegistry"`. After addition, users can install Neuroblox.jl similarly to any other Julia package via commands like `Pkg.add("Neuroblox")` or through the package manager REPL interface (`pkg> add Neuroblox`). The registry is temporary and can be removed using `pkg"registry remove NeurobloxRegistry"` or by manually deleting the corresponding file in the `.julia/registries` directory if needed.

KEYWORDS:
NeurobloxRegistry, Julia, package registry, Neuroblox.jl, installation command, pkg add, removal command, depot path.
