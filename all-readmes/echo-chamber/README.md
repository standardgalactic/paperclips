# echo-chamber

[Echo Chamber](https://standardgalactic.github.io/echo-chamber/echo-chamber.pdf)

An experimental information architecture in which Git branches are
used instead of files, directories, pages, chapters, headings,
footnotes, hyperlinks, or good judgment.

The repository is intentionally inconvenient.

It currently contains **256 mutually isolated reading
environments**.

## Reading

The main branch contains almost nothing.

To inspect the actual material:

```bash
git branch -a
```

Then choose a chamber:

```bash
git switch chamber/0001
```

To read another page:

```bash
git switch chamber/0002
```

The working tree will be replaced with the next fragment.

## Why?

Because a branch can contain a document.

Therefore, by an impeccable chain of reasoning, a branch should
contain a document.

## Conventional architecture

```text
book/
├── chapter-01.md
├── chapter-02.md
├── chapter-03.md
└── chapter-04.md
```

## echo-chamber architecture

```text
main
chamber/0001
chamber/0002
chamber/0003
chamber/0004
...
chamber/0256
```

Each chamber is an orphan branch.

The chapters therefore do not merely occupy different locations.

They inhabit unrelated histories.

## Table of contents

```bash
git branch
```

## Search

First determine which universe contains the text.

Then enter that universe.

Then search it.

## Multiple pages

Use `git worktree`.

This converts reading comprehension into repository administration.

## Design principle

> If a directory can solve the problem, introduce another dimension.
