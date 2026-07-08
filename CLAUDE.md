# Skills Repository Guide

This repository contains Claude Skills for extending Claude's capabilities with specialized knowledge, workflows, and tools.

## Quick Reference

### Common Tasks
- **Create new skill**: Use the `skill-creator` skill with concrete examples
- **Update existing skill**: Edit SKILL.md and bundled resources, then package
- **Validate skill**: Run `scripts/package_skill.py <skill-path>` (validates automatically)
- **Test skill**: Load in Claude and test with real-world scenarios

### Repository Structure
```
skills-repository/
├── skill-name/
│   ├── SKILL.md (required)
│   ├── scripts/ (optional - executable code)
│   ├── references/ (optional - docs loaded as needed)
│   └── assets/ (optional - files used in output)
└── scripts/
    ├── init_skill.py (creates new skill template)
    └── package_skill.py (validates and packages skills)
```

## Creating Skills

### Use the skill-creator Skill

Always use the `skill-creator` skill when developing new skills or updating existing ones. It provides comprehensive guidance on the skill creation process.

**Trigger the skill by stating**: "I want to create a new skill" or "Help me build a skill for [purpose]"

### Core Principles

**Concise is key**: Only include information Claude doesn't already know. Challenge each piece of content—does it justify its token cost?

**Progressive disclosure**: Structure skills in three levels:
1. Metadata (always loaded)
2. SKILL.md body (loaded when triggered)
3. Bundled resources (loaded as needed)

**Imperative form**: Write all instructions using verb-first commands ("To accomplish X, do Y"), not second person ("You should...").

## Skill Quality Standards

### YAML Frontmatter Requirements
```yaml
---
name: skill-name  # lowercase, hyphens only, max 64 chars
description: "Specific description of what skill does and when to use it. Include key terms and trigger contexts. Write in third person."
---
```

### Description Quality Checklist
- [ ] Written in third person
- [ ] Describes what the skill does
- [ ] Describes when to use it
- [ ] Includes key terms for discoverability
- [ ] Under 1024 characters
- [ ] Specific, not vague

**Good example**:
```yaml
description: "Processes Excel files and generates reports with pivot tables and charts. Use when analyzing spreadsheets, .xlsx files, or when user mentions Excel, pivot tables, or tabular data analysis."
```

**Bad example**:
```yaml
description: "Helps with documents"
```

### SKILL.md Body Guidelines

**Keep under 500 lines**: If approaching this limit, split content into reference files.

**Structure for navigation**:
- Start with clear purpose statement
- Provide workflow overviews
- Reference detailed materials as needed
- Use consistent terminology throughout

**Avoid**:
- Time-sensitive information (dates, version-specific details)
- Over-explaining concepts Claude already knows
- Windows-style paths (use forward slashes)
- Offering too many alternatives (provide defaults with escape hatches)

## Bundled Resources

### scripts/ - Executable Code

**When to include**: Tasks requiring deterministic reliability or repeatedly rewritten code.

**Benefits**:
- Token efficient (can execute without loading into context)
- More reliable than generated code
- Ensures consistency

**Requirements**:
- Handle errors explicitly (don't punt to Claude)
- No "magic numbers" (document all constants)
- Include clear usage documentation in SKILL.md

### references/ - Documentation

**When to include**: Detailed information Claude should reference while working.

**Use cases**:
- Database schemas
- API documentation  
- Company policies
- Domain knowledge
- Detailed workflow guides

**Best practices**:
- Keep information in either SKILL.md OR references/, not both
- For files >10k words, include grep search patterns in SKILL.md
- Structure with table of contents for files >100 lines
- Keep references one level deep from SKILL.md

### assets/ - Output Resources

**When to include**: Files used in final output, not loaded into context.

**Use cases**:
- Templates (PPTX, DOCX, HTML)
- Brand assets (logos, fonts)
- Boilerplate code
- Sample documents

## Workflows

### Creating a New Skill

1. **Gather examples**: Understand concrete use cases
   - "What functionality should this skill support?"
   - "Can you give examples of how this would be used?"
   - "What would trigger this skill?"

2. **Plan resources**: For each example, identify:
   - Scripts that would avoid rewriting code
   - References that provide needed context
   - Assets that would be used in outputs

3. **Initialize**: Run `scripts/init_skill.py <skill-name> --path <output-dir>`

4. **Implement**: 
   - Create scripts, references, and assets
   - Delete unused example files
   - Update SKILL.md to reference resources

5. **Package**: Run `scripts/package_skill.py <path/to/skill-folder>`

6. **Iterate**: Test with real tasks and refine

### Updating an Existing Skill

1. **Use the skill**: Test on real tasks
2. **Observe struggles**: Note where Claude struggles or succeeds
3. **Identify improvements**: Determine what should change
4. **Edit resources**: Update SKILL.md, scripts, references, or assets
5. **Repackage**: Run `scripts/package_skill.py <path/to/skill-folder>`
6. **Test changes**: Verify improvements on similar tasks

### Contributing to Repository

**Commit workflow**:
1. Make changes to skill
2. Validate: `scripts/package_skill.py <skill-path>`
3. Test skill with real scenarios
4. Commit with descriptive message
5. Create PR with:
   - What the skill does
   - Example use cases
   - Testing performed

**Commit message format**:
```
feat(skill-name): brief description

Detailed explanation of changes and reasoning
```

# Releasing

## Version control

Use [semantic versioning](https://semver.org/) to provide a reliable label to each version of each skill. Given a version number `MAJOR.MINOR.PATCH`, increment the:

* MAJOR version when you make incompatible changes to the instructions;
* MINOR version when you add functionality in a backward compatible manner;
* PATCH version when you make negligible alterations and backward compatible bug fixes.

The version should be included in the front-matter of each `SKILL.md` file in the `version` key, for example:

```yaml
version: 0.1.0
```

## Common Patterns

### Workflow Pattern with Checklist

For multi-step processes, provide a checklist Claude can track:

````markdown
## Task workflow

Copy this checklist and track progress:

```
- [ ] Step 1: Action description
- [ ] Step 2: Action description  
- [ ] Step 3: Action description
```

**Step 1: Action description**
Detailed instructions...

**Step 2: Action description**
Detailed instructions...
````

### Validation Loop Pattern

For quality-critical tasks:

```markdown
## Editing process

1. Make edits to target files
2. Validate: `python scripts/validate.py`
3. If validation fails:
   - Review error messages
   - Fix issues
   - Validate again
4. Only proceed when validation passes
5. Execute final step
```

### Conditional Workflow Pattern

For tasks with decision points:

```markdown
## Processing workflow

1. Determine task type:
   
   **Creating new?** → Follow creation workflow below
   **Editing existing?** → Follow editing workflow below

2. Creation workflow:
   - Step A
   - Step B
   
3. Editing workflow:
   - Step X
   - Step Y
```

### Template Pattern

For structured outputs:

````markdown
## Output structure

ALWAYS use this template:

```markdown
# [Title]

## Section 1
Content guidelines...

## Section 2
Content guidelines...
```
````

## Skill Maintenance

### Regular Reviews

Periodically review skills for:
- Outdated information
- Unused bundled resources
- Opportunities for consolidation
- Missing common use cases

### Quality Metrics

Good skills demonstrate:
- Clear, specific descriptions
- Concise SKILL.md bodies
- Well-organized bundled resources
- Validation passing
- Real-world testing
- Consistent terminology
- Progressive disclosure usage

### Testing Approach

Test skills by:
1. Using with fresh Claude instance
2. Testing with real scenarios (not synthetic examples)
3. Observing which files Claude accesses
4. Noting unexpected behaviors
5. Gathering feedback from actual users

## Anti-Patterns to Avoid

- **Verbose explanations**: Don't explain what Claude already knows
- **Nested references**: Keep references one level deep from SKILL.md
- **Magic numbers**: Document all configuration values
- **Punting errors**: Handle errors in scripts, don't defer to Claude
- **Too many options**: Provide defaults with escape hatches
- **Inconsistent terms**: Use same terminology throughout
- **Time-sensitive info**: Use "old patterns" sections for deprecated content
- **Windows paths**: Always use forward slashes

## Resources

- **skill-creator skill**: Comprehensive guidance on skill creation process
- **init_skill.py**: Template generator for new skills
- **package_skill.py**: Validation and packaging tool
- Anthropic Skills documentation: https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/

## Quick Validation Checklist

Before packaging any skill:

- [ ] Description is specific and includes key terms
- [ ] Description written in third person
- [ ] SKILL.md body under 500 lines
- [ ] Consistent terminology throughout
- [ ] No time-sensitive information
- [ ] Scripts handle errors explicitly
- [ ] File references one level deep
- [ ] Forward slashes in all paths
- [ ] Tested with real scenarios
- [ ] Validation passes (automatic via package script)