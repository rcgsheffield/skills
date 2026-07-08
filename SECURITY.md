# Security Policy

## Overview

This repository contains Claude Code skills that extend Claude's capabilities. Security is a shared responsibility between skill developers, maintainers, and users. This policy outlines our security practices and guidelines.

## Reporting Security Vulnerabilities

If you discover a security vulnerability, please **do not** open a public GitHub issue. Instead:

1. Email security concerns to [your-email@example.com]
2. Include a clear description of the vulnerability
3. Provide steps to reproduce (if applicable)
4. Allow up to 90 days for a fix before public disclosure

We take all security reports seriously and will acknowledge receipt within 48 hours.

## Security Principles

### 1. Principle of Least Privilege

Skills should only request the minimum permissions necessary to function. When defining `allowed-tools` in `SKILL.md`:

- Explicitly restrict file access to necessary directories
- Avoid blanket permissions like `Bash(*)`
- Use read-only access when write access isn't required
- Document why each permission is needed

Example:
```yaml
allowed-tools:
  - Bash(git status, git log)
  - Edit(docs/*, .claude/skills/*)
```

### 2. Input Validation

All skills must validate external inputs:

- Sanitize user prompts before passing to external APIs
- Validate file paths to prevent directory traversal attacks
- Check data types and formats before processing
- Use explicit allow-lists rather than block-lists for accepted inputs

### 3. Secure Defaults

- Scripts run with minimal permissions by default
- Skills fail safely (deny by default)
- Sensitive operations require explicit user confirmation
- No credentials or secrets in skill code or templates

## Skill Development Guidelines

### Handling Credentials and Secrets

- **Never** hardcode API keys, tokens, or passwords
- Use environment variables for sensitive configuration
- Document required credentials in SKILL.md with setup instructions
- Consider using `.env` files (always add to `.gitignore`)
- Test that skills work with proper credential management

### External Dependencies

- Keep dependencies up to date
- Document all external dependencies in the skill's documentation
- Use version pinning for critical dependencies
- Verify the integrity of third-party tools before use
- Avoid unnecessary dependencies

### File Operations

- Always validate file paths to prevent directory traversal
- Use absolute paths when possible
- Clearly document which directories a skill accesses
- Restrict write operations to specific directories
- Be cautious with recursive operations (deletion, chmod)

### Code Quality and Review

- All skills should undergo security review before merging
- Code should be readable and well-commented
- Remove debug code and verbose logging before release
- Follow language-specific security best practices
- Test error handling paths

## Skill User Guidelines

### Before Using a Skill

1. Read the `SKILL.md` description and instructions
2. Review any scripts or supporting files
3. Understand what permissions the skill requests
4. Check the skill's allowed-tools restrictions
5. Verify the source is trusted

### Permission Review

- Always review permission requests from Claude
- Don't blindly grant permissions with "always allow"
- Use `--dangerously-skip-permissions` only in isolated environments
- Be especially cautious with skills that:
  - Access sensitive directories
  - Run arbitrary bash commands
  - Interact with external services
  - Modify critical system files

### Running Skills Safely

- Run unfamiliar skills in isolated environments first
- Keep backups before running skills with write access
- Monitor skill behavior during execution
- Use containers or VMs for high-risk operations
- Don't run skills from untrusted sources in production environments

## Secure Skill Templates

When creating new skills, use these templates as starting points:

### Safe File Reading Skill
```markdown
---
name: Safe File Reader
description: Read and analyze text files with path validation
allowed-tools:
  - Bash(head, tail, wc)
---

# Instructions

Always validate file paths:
- No paths containing ".."
- No absolute paths outside the project
- Confirm the file type matches expectations
```

### Safe API Integration Skill
```markdown
---
name: API Integrator
description: Safely call external APIs with credential handling
allowed-tools:
  - Bash(curl)
---

# Instructions

- Only use credentials from environment variables
- Validate all URLs before making requests
- Never log request/response bodies containing secrets
- Use HTTPS only
```

## Security Monitoring and Updates

### Keeping Skills Secure

- Monitor dependencies for security updates
- Subscribe to security advisories for technologies your skills use
- Review and update skills quarterly
- Document security updates in version history

### Community Reporting

If you discover a security issue in an existing skill:

1. Report it privately first (don't open public issues)
2. Allow time for maintainers to fix it
3. Coordinate disclosure timing
4. Help verify the fix works

## Compliance

Skills in this repository should comply with:

- **Data Privacy**: Respect user data; don't collect or transmit unnecessary information
- **Licensing**: Ensure all dependencies have compatible licenses
- **Standards**: Follow relevant security standards for your domain (OWASP, CWE, etc.)

## Version Control and Audit Trail

- All skill changes are tracked in git
- Commit messages should reference security issues when applicable
- Security-related changes should be clearly marked
- Maintain a CHANGELOG documenting security fixes

Example:
```
security: fix path traversal vulnerability in file-reader skill
- Validate file paths against allow-list
- Reject paths containing ".."
- Add unit tests for path validation
```

## Resources

- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code/skills)
- [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)

## Policy Updates

This security policy may be updated at any time. Major changes will be communicated to contributors. The policy is effective immediately upon commit.
