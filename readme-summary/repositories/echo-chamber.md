# echo-chamber

Summary:

The echo-chamber repository implements an experimental information architecture using Git branches instead of traditional file and directory structures. It contains 256 isolated "chambers" (branches), each representing a distinct reading environment. The main branch is intentionally minimal; to access content, users must switch to specific chambers via `git switch chamber/<number>`. Each chamber holds a single document fragment, emphasizing that branches can contain documents rather than just files. This design breaks away from conventional hierarchical structures by having chapters inhabit unrelated histories and locations. Navigation involves listing all branches with `git branch` and using `git worktree` for handling multiple pages. The project's core principle is to introduce additional dimensions (branches) when a directory alone cannot solve the problem of organizing information.

KEYWORDS:
echo chamber, Git branches, experimental architecture, reading environments, chambers, repository structure, unconventional design, git switch, git branch, worktree
