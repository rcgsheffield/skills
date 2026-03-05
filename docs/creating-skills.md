# Building Skills: A Practical Guide

This guide covers how to design, structure, and write high-quality skills. For submission and quality checklists, see [CONTRIBUTING.md](../CONTRIBUTING.md).

## What goes in a skill

A skill packages knowledge Claude doesn't already have — your organisation's conventions, domain-specific workflows, templates, and reference data. It does **not** need to teach Claude general concepts it already knows.

Ask for each piece of content: _does this justify its token cost?_ If Claude would produce a reasonable answer without the skill, leave it out.

## Anatomy of a skill

```
skill-name/
├── SKILL.md          # required — instructions + frontmatter
├── scripts/          # optional — executable code for deterministic tasks
├── references/       # optional — detailed docs loaded on demand
└── assets/           # optional — templates and output files
```

### SKILL.md

The entry point. Contains YAML frontmatter and the main instructions.

```markdown
---
name: skill-name
description: "What it does and when to use it. Written in third person. Include trigger contexts."
version: 0.1.0
domain: category
---

# Skill Title

Brief purpose statement.

## Workflow

Step-by-step instructions...
```

Keep the body **under 500 lines**. Move detailed reference material into `references/`.

### scripts/

Include scripts when a task must be deterministic or would otherwise be rewritten from scratch each time (e.g. validation, packaging, code generation).

Requirements:

- Handle errors explicitly — do not defer to Claude
- Document all constants and configuration values
- Include usage instructions in SKILL.md

### references/

Detailed documentation Claude should consult while working: schemas, API docs, policies, domain knowledge. Load references on demand rather than embedding everything in SKILL.md.

- Keep one level deep from SKILL.md (no nested reference directories)
- For files over 100 lines, add a table of contents
- Store information in either SKILL.md _or_ a reference file, not both

### assets/

Files used in outputs, not loaded into context: templates (DOCX, PPTX, HTML), brand assets, boilerplate code, sample documents.

## Writing effective instructions

**Use imperative form.** Write `"To accomplish X, do Y"` not `"You should..."`.

**Progressive disclosure.** Structure content in three levels:

1. Frontmatter metadata — always loaded, must be concise
2. SKILL.md body — loaded when the skill triggers
3. Bundled resources — loaded only when needed

**Provide defaults.** Pick one approach and document it. Offer alternatives only where the choice genuinely matters to the user.

**Avoid time-sensitive content.** Do not include version numbers, dates, or information that will go stale.

## Workflow patterns

### Multi-step process with checklist

````markdown
## Task workflow

Copy and track this checklist:

```
- [ ] Step 1
- [ ] Step 2
- [ ] Step 3
```

**Step 1:** ...

**Step 2:** ...
````

### Validation loop

```markdown
## Editing process

1. Make changes
2. Run: `python scripts/validate.py`
3. If validation fails, fix errors and validate again
4. Proceed only when validation passes
```

### Conditional workflow

```markdown
## Workflow

1. Determine task type:

   **Creating?** Follow the creation workflow.
   **Editing?** Follow the editing workflow.

2. Creation workflow: ...

3. Editing workflow: ...
```

## Common mistakes

| Mistake                                   | Fix                                          |
| ----------------------------------------- | -------------------------------------------- |
| Explaining what Claude already knows      | Remove it — only include proprietary context |
| Putting everything in SKILL.md            | Move detail into `references/`               |
| Nested reference directories              | Keep references one level deep               |
| Magic numbers in scripts                  | Document all constants                       |
| Windows-style paths                       | Use forward slashes everywhere               |
| Time-sensitive information (dates, vers.) | Remove or use "current" language             |
| Too many alternatives                     | Pick a default, note the escape hatch        |

## Version numbering

Use [semantic versioning](https://semver.org/):

- **MAJOR** — incompatible instruction changes
- **MINOR** — new functionality, backwards compatible
- **PATCH** — minor fixes and corrections

Set the version in frontmatter: `version: 0.1.0`

## Testing

Test skills with real scenarios, not synthetic examples:

1. Use the skill with a fresh Claude instance
2. Note where Claude hesitates or produces unexpected output
3. Identify missing context or ambiguous instructions
4. Update the skill and retest

## Further reading

- [Skill authoring best practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices)
- [Agent Skills overview](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
- Use the `skill-creator` skill for interactive guidance
