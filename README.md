# Agent skills

Agent Skills are **modular capabilities** that package expertise to extend their functionality. This repository collection of these structured prompts for repeated complex tasks that AI chatbots and agents can follow. For background, please read [Introducing Agent Skills](https://www.anthropic.com/news/skills) by Anthropic and the Claude documentation on [Agent Skills](https://docs.claude.com/en/docs/claude-code/skills).

Skills are selected and used by the AI models agentically without human intervention. Unlike user-invoked commands, the chatbot autonomously decides when to use a Skill based on the user's request and the Skill's description.

## Benefits

Skills are useful for making agents more efficiently perform repeated tasks that require structured prompting.

- Extend agents for specific, custom workflows;
- Reduce repetitive prompting;
- Share expertise with others;
- Compose multiple Skills for complex tasks.

## Contributing

We welcome contributions to this skills repository. Please see [the contribution guide](CONTRIBUTING.md) for detailed guidelines on creating, testing, and submitting skills. For internal skills specific to our organisation, submit a pull request to propose a change or write a new skill.

### Sharing skills

The recommended approach is to distribute skills through [Claude Code plugins](https://docs.claude.com/en/docs/claude-code/plugins), but you can also share directly by committing skills to your project repository in `.claude/skills/` so teammates automatically get them when they pull changes. There are several public repositories for sharing plugins, skills, subagents, and other extensions for agentic tools such as Claude Code such as Anthropic's skills repository [anthropics/skills](https://github.com/anthropics/skills).

## Writing skills

Please write [How Skills Work](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview#how-skills-work) from the Claude documentation.

There is a meta-skill for writing skills called [skill-creator](https://github.com/anthropics/skills/tree/main/skill-creator) provided by Anthropic to help you write high-quality skills.

### Best practices

Please read [Skill authoring best practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices) by Anthropic and our [guide to building skills](docs/creating-skills.md).

Treat skills like production code. They need proper tooling, testing, documentation, and governance to scale reliably in organisations and teams.

- **Keep Skills focused:** Each Skill should address _one capability_ and be specific to avoid you having to repeat complex, structured prompts. Write clear descriptions that help Claude discover when to use Skills by including specific triggers.
- **Clear descriptions:** The description is vital as it tells the agent what the Skill does and when to use it. The description should include both what the Skill does and when Claude should use it. 
- **Resource Management:** Skills need to be designed with token efficiency in mind. Consider chunking strategies and avoiding loading unnecessary context.

- **Code Quality & Testing:** Treat skills like ["code we can read in plain English"](https://natesnewsletter.substack.com/p/i-watched-100-people-hit-the-same). There are testing frameworks for skills to ensure they work consistently.

- **Security Evaluation:** Always vet third-party skills. Skill auditing practices are required.

- **Version control:** Like with software, skills are reusable and sharable components designed to optimise repeatable tasks. We expect to modify and improve them over their lifecycle. To make the challenge of divergent versions tractable, use a [semantic version control scheme](https://semver.org/) to label each skill.

### Directory structure

The [`skills/` directory](./skills/) contains a series of subdirectories, one per skill. Each has a `SKILL.md` file with YAML frontmatter (metadata including a name and a crucial description) and Markdown content providing step-by-step instructions. They can also include optional supporting files like scripts and templates. 

This repository is designed to be copied into your skills configuration or imported into your agent software. It has the following directory structure:

```tree
~/.claude/skills/
├── skill-name-1/
│   ├── SKILL.md
│   ├── scripts/
│   └── templates/
└── skill-name-2/
    └── SKILL.md
```

