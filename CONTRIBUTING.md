# Contributing to Skills Repository

Thank you for contributing to this skills repository. This guide covers how to create, update, and submit skills.

## Report a problem or request a change

Please [create an issue](https://github.com/rcgsheffield/skills/issues/new) to request a change or report a problem.

## Quick Start

1. **Create new skill**: Use the `skill-creator` skill or use the initial template below
2. **Test thoroughly**: Load in Claude and test with real scenarios
3. **Validate**: Run `scripts/package_skill.py <skill-path>` before submitting
4. **Submit PR**: Include description, use cases, and testing evidence

## Creating a New Skill

### 1. Gather Requirements
- Identify concrete use cases
- Determine trigger contexts
- Plan bundled resources (scripts, references, assets)

### 2. Initialize Skill

Create the `SKILL.md`  file using the template below

```markdown
---
name: <Skill name>
description: <Skill description>
version: 0.1.0
domain: <Categories or tags>
---
# Title
...
## Heading
...
```

### 3. Implement Skill
- Edit `SKILL.md` with clear instructions
- Add scripts for deterministic tasks (optional)
- Include references for detailed documentation (optional)
- Add assets for templates or output files (optional)
- Delete unused example files

### 4. Write Quality Description
Description must:
- Be written in third person
- Describe what the skill does AND when to use it
- Include key terms for discoverability
- Be under 1024 characters
- Be specific, not vague

**Good example**:
```yaml
description: "Processes Excel files and generates reports with pivot tables and charts. Use when analyzing spreadsheets, .xlsx files, or when user mentions Excel, pivot tables, or tabular data analysis."
```

### 5. Validate and Test
```bash
python scripts/package_skill.py skills/<skill-name>
```
Test with real scenarios in Claude before submitting.

## Updating Existing Skills

1. Test skill with real tasks
2. Identify improvements based on observations
3. Edit `SKILL.md` and bundled resources
4. Repackage: `scripts/package_skill.py <skill-path>`
5. Test changes before submitting

## Quality Standards

### Required Checks
- [ ] YAML frontmatter complete (name, description)
- [ ] Description in third person with trigger contexts
- [ ] SKILL.md body under 500 lines
- [ ] Consistent terminology throughout
- [ ] No time-sensitive information
- [ ] Scripts handle errors explicitly
- [ ] Forward slashes in all paths
- [ ] Validation passes
- [ ] Tested with real scenarios

### Content Guidelines
- **Be concise**: Only include what Claude doesn't already know
- **Use imperatives**: "Do X to achieve Y" (not "You should...")
- **Progressive disclosure**: Metadata → SKILL.md → Bundled resources
- **One level deep**: Keep references one level from SKILL.md

### Avoid
- Over-explaining concepts Claude knows
- Time-sensitive information (dates, versions)
- Windows-style paths
- "Magic numbers" in scripts
- Nested reference structures

## Submitting Changes

### Commit Format
```
feat(skill-name): brief description

Detailed explanation of changes and reasoning
```

### Pull Request Template
Include:
1. **What**: Description of the skill/changes
2. **When**: Example trigger contexts
3. **Testing**: Real scenarios tested and results
4. **Resources**: List of bundled files and their purpose

### Review Process
1. Automated validation runs on PR
2. Maintainers review for quality and fit
3. Testing feedback may be requested
4. Merge after approval

## Resources

- [Agent Skills Documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/)
- [Skill Authoring Best Practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices)
- [Creating Skills Guide](docs/creating-skills.md)
- Use the `skill-creator` skill for comprehensive guidance

## Questions?

- Check the [README](README.md) for overview
- Read [CLAUDE.md](CLAUDE.md) for detailed guidelines
- Review existing skills in `skills/` for examples
- Use the `skill-creator` skill for interactive help
