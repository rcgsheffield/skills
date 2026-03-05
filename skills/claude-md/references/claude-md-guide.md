# Writing Effective CLAUDE.md Files for Claude Code

A practical guide synthesising Anthropic's official documentation, the research paper
_Evaluating AGENTS.md_ (Gloaguen et al., 2026), and community best practices.

---

## The Core Insight: Less Is More

The single most important finding from empirical research is counterintuitive:
**more instructions tend to hurt, not help**. The 2026 study from ETH Zurich found that
LLM-generated context files _reduced_ agent task-success rates and increased inference
cost by over 20%. Human-written files only marginally improved performance — and only
when they contained minimal, actionable requirements.

Why? Unnecessary instructions make tasks cognitively harder for the agent. Claude Code's
own system prompt already consumes roughly 50 of the ~150–200 instructions a frontier
model can reliably follow. Every line you add to `CLAUDE.md` competes for that budget.

---

## What CLAUDE.md Is For

`CLAUDE.md` is read at the start of **every** conversation. Its job is to onboard Claude
to your codebase — specifically the things it cannot infer by reading the code itself.

Cover three things and nothing more:

| Dimension | Question to answer                                                 |
| --------- | ------------------------------------------------------------------ |
| **WHAT**  | What is this codebase? Tech stack, repo structure, key directories |
| **WHY**   | What is its purpose? What do the major components do?              |
| **HOW**   | How does work get done? Build, test, lint commands; tooling quirks |

---

## The Seven Rules

### 1. Keep it short and universally applicable

Every line is injected into every session, relevant or not. Aim for **under 100 lines**
for a typical project. Under 60 is better. Only include instructions that apply to
virtually every task you will ever ask Claude to do in this codebase.

> If an instruction only matters when working on database schemas, it does not belong in
> `CLAUDE.md`. It belongs in `agent_docs/database_schema.md` (see Rule 4).

### 2. Never include code style guidelines

Do not use Claude as an expensive, slow linter. LLMs are in-context learners — if your
codebase follows a consistent style, Claude will match it from examples alone. Code style
instructions waste your instruction budget and context window on every task, including
ones where formatting is irrelevant.

Instead:

- Use a deterministic linter/formatter (e.g. `ruff`, `biome`, `prettier`)
- Automate it via a **Stop hook** so Claude's edits are formatted automatically
- Or create a `/lint` slash command to invoke style checks on demand

### 3. Use progressive disclosure

Rather than embedding all project knowledge in one file, keep `CLAUDE.md` lean and point
Claude at a library of supplementary documents:

```
agent_docs/
  building_the_project.md
  running_tests.md
  service_architecture.md
  database_conventions.md
  deployment_process.md
```

In `CLAUDE.md`, list these files with one-line descriptions and instruct Claude to read
whichever are relevant before starting. This way the context window is only loaded with
information that matters for the current task.

### 4. Prefer pointers to copies

Never paste code snippets or configuration examples directly into `CLAUDE.md`. They
become stale immediately. Instead, reference the canonical location:

```
# Testing
See agent_docs/running_tests.md.
The test runner is configured in pyproject.toml (tool.pytest section).
```

File-and-line references (`src/auth/service.py:42`) are more useful and less wasteful
than inline examples.

### 5. Include only the commands Claude cannot discover itself

Good candidates for `CLAUDE.md`:

- Non-obvious tooling (e.g. `uv` instead of `pip`, `bun` instead of `npm`)
- Project-specific scripts that have no standard equivalent
- How to run the test suite and verify changes
- Environment setup that is genuinely unusual

Do **not** include:

- `git status`, `ls`, `cat` — Claude knows these
- Obvious commands it can discover from `package.json`, `Makefile`, or `pyproject.toml`
- Long lists of every possible command

### 6. Write it yourself — do not auto-generate it

Running `/init` or using a prompt to auto-generate `CLAUDE.md` produces a file that
mirrors existing documentation (which Claude can already read) and pads it with
boilerplate. Research confirms these LLM-generated files perform no better than having
no file at all, and often perform worse.

`CLAUDE.md` is the highest-leverage configuration point in your entire Claude Code
setup. Spend time on it deliberately. Each line affects every conversation you will
ever have in that project.

### 7. Evolve it incrementally

Start minimal. After each working session, if you notice Claude repeatedly making a
wrong assumption or needing correcting on the same point, add **one** concise instruction
to address it. Remove instructions that are no longer applicable. Treat it like
production code: subject to review, not a dumping ground.

---

## The Recommended Structure

```markdown
# [Project Name]

## Purpose

[One to three sentences: what this project does and why it exists.]

## Repository Layout

[Brief directory map — only non-obvious structure. Skip if standard.]
src/ # Application code
tests/ # Test suite
agent_docs/ # Extended documentation for Claude — read relevant files before starting

## Key Tooling

- Runtime: [e.g. Python 3.12 via uv, not pip]
- Test runner: [e.g. pytest — run with `uv run pytest`]
- Linter: [e.g. ruff — runs automatically on save via hook]
- Build: [e.g. `make build`]

## Verification

Before considering a task complete:

1. Run the test suite: [command]
2. Run the type checker: [command]

## Extended Documentation

Read the relevant file(s) before starting work on the following topics:

- Architecture and service boundaries → agent_docs/architecture.md
- Database conventions → agent_docs/database_conventions.md
- Deployment → agent_docs/deployment.md
- [Add others as needed]
```

---

## Hierarchical Files

Claude Code supports `CLAUDE.md` at multiple levels. Use this to keep context scoped:

```
CLAUDE.md                  # Project-wide: always loaded
src/payments/CLAUDE.md     # Loaded only when working in that directory
src/ml/CLAUDE.md           # Loaded only when working in that directory
```

Subdirectory files should be even more concise than the root — they only need to capture
what is unique and non-obvious about that part of the codebase.

---

## What NOT to Put in CLAUDE.md

| ❌ Avoid                                               | ✅ Instead                          |
| ------------------------------------------------------ | ----------------------------------- |
| Code style rules                                       | Configure a linter; use a Stop hook |
| Large code snippets                                    | Reference the file and line         |
| Instructions only relevant to one task type            | Put them in `agent_docs/`           |
| Generic reminders ("be careful", "think step by step") | Trust the model                     |
| Exhaustive command lists                               | Include only non-obvious ones       |
| Auto-generated overviews of directory structure        | Claude can run `ls`                 |
| Anything that duplicates existing README/docs          | Point to those files instead        |

---

## A Note on Instruction Following

Claude Code wraps `CLAUDE.md` contents in a system reminder that tells the model to
ignore instructions that are not relevant to the current task. This is intentional.
The implication is direct: **if an instruction is not universally applicable, it will
often be ignored**. The remedy is not to write more forceful instructions — it is to
write fewer, better-targeted ones.

---

## Quick-Start Checklist

- [ ] Written by hand, not auto-generated
- [ ] Under 100 lines (ideally under 60)
- [ ] Covers WHAT, WHY, and HOW
- [ ] Contains only universally applicable content
- [ ] No code style rules (delegate to a linter)
- [ ] No copy-pasted code snippets
- [ ] Points to `agent_docs/` for topic-specific detail
- [ ] Includes the test/verify command(s)
- [ ] Lists non-obvious tooling choices
- [ ] Reviewed and pruned after the first few sessions

---

_Sources: Gloaguen et al. (2026) "Evaluating AGENTS.md", Anthropic Claude Code
documentation, HumanLayer "Writing a good CLAUDE.md", Trail of Bits claude-code-config._
