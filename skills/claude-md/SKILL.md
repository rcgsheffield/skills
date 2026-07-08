---
name: claude-md
version: 0.1.0
description: "Guides writing effective CLAUDE.md files for Claude Code projects. Use when a user wants to create, improve, or audit a CLAUDE.md file, asks what to put in CLAUDE.md, or wants to configure Claude Code for a project. Covers content strategy, structure, anti-patterns, progressive disclosure, and hierarchical placement."
---

# CLAUDE.md Writer

Helps create effective `CLAUDE.md` files that onboard Claude to a codebase without wasting context.

## Core principle

More instructions hurt performance. Every line in `CLAUDE.md` is injected into every session, consuming the model's limited instruction budget. Write the minimum needed to cover what Claude cannot infer from the code itself.

A good `CLAUDE.md` answers exactly three questions:

| Dimension | Question                                                           |
| --------- | ------------------------------------------------------------------ |
| WHAT      | What is this codebase? Tech stack, repo structure, key directories |
| WHY       | What is its purpose? What do the major components do?              |
| HOW       | How does work get done? Build, test, lint commands; tooling quirks |

## Workflow

### Step 1: Audit the project

Before writing, read the following to understand what Claude can already discover:

- `README.md`, `package.json`, `pyproject.toml`, `Makefile` — standard tooling
- Directory listing — obvious structure
- Existing `CLAUDE.md` if present — what to keep or cut

### Step 2: Identify what Claude cannot discover itself

Include only:

- Non-standard tooling (`uv` not `pip`, `bun` not `npm`, `just` not `make`)
- Non-obvious test/verify commands
- Project-specific scripts with no standard equivalent
- Unusual environment setup

Exclude:

- `git status`, `ls`, `cat` — Claude knows these
- Commands discoverable from `package.json` or `Makefile`
- Code style rules (delegate to a linter)
- Inline code snippets (reference the file instead)
- Generic reminders ("be careful", "think step by step")

### Step 3: Write using the recommended structure

```markdown
# [Project Name]

## Purpose

[One to three sentences: what this project does and why it exists.]

## Repository Layout

[Brief directory map — only non-obvious entries.]
src/ # Application code
agent_docs/ # Extended docs for Claude — read relevant files before starting

## Key Tooling

- Runtime: [e.g. Python 3.12 via uv, not pip]
- Test runner: [e.g. pytest — run with `uv run pytest`]
- Linter: [runs automatically via hook]

## Verification

Before considering a task complete:

1. [Test command]
2. [Type check or lint command if not automated]

## Extended Documentation

Read the relevant file before starting work on:

- Architecture → agent_docs/architecture.md
- Database conventions → agent_docs/database.md
```

### Step 4: Apply the seven rules

See `claude-md-guide.md` for full detail. Summarised:

1. **Keep it short** — under 100 lines; under 60 is better
2. **No code style rules** — use a linter and automate it
3. **Progressive disclosure** — point to `agent_docs/` for topic-specific detail
4. **Prefer pointers** — reference files/lines, never paste snippets
5. **Only non-obvious commands** — skip discoverable ones
6. **Write it yourself** — do not auto-generate with `/init` or prompts
7. **Evolve incrementally** — add one line per repeated correction; prune regularly

### Step 5: Consider hierarchical placement

```
CLAUDE.md                   # Project-wide: loaded always
src/payments/CLAUDE.md      # Loaded only when working in that directory
src/ml/CLAUDE.md            # Loaded only when working in that directory
```

Subdirectory files should be even more concise — only what is unique to that subtree.

### Step 6: Validate with the checklist

```
- [ ] Written by hand, not auto-generated
- [ ] Under 100 lines (ideally under 60)
- [ ] Covers WHAT, WHY, and HOW
- [ ] Contains only universally applicable content
- [ ] No code style rules
- [ ] No copy-pasted code snippets
- [ ] Points to agent_docs/ for topic-specific detail
- [ ] Includes test/verify command(s)
- [ ] Lists non-obvious tooling choices
- [ ] Reviewed and pruned after the first few sessions
```

## Reference

For full detail on every rule, the research behind the recommendations, and the complete anti-pattern table, read `references/claude-md-guide.md`.
