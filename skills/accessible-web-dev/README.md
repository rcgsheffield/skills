# University of Sheffield Web Accessibility Skill

## Overview

The University of Sheffield Web Accessibility Skill is a comprehensive Claude Skill designed to ensure web applications, digital platforms, and content meet institutional accessibility policies and WCAG 2.1 AA/AAA compliance standards. This skill provides proactive guidance throughout the development lifecycle, from initial planning through deployment and maintenance.

## Purpose

This skill addresses a critical need in web development: building accessibility into applications from the start rather than retrofitting it later. By encoding the University of Sheffield's accessibility requirements, WCAG standards, and industry best practices into a reusable skill, teams can:

- **Build accessible applications proactively** during development, not reactively during remediation
- **Maintain consistent compliance** across all digital platforms and projects
- **Reduce costs** by avoiding expensive accessibility retrofits
- **Ensure legal compliance** with UK public sector accessibility regulations
- **Create inclusive experiences** that benefit all users, regardless of ability

## When to Use This Skill

Invoke this skill **proactively** when:

- Planning new features or applications
- Building UI components, forms, or interactive elements
- Designing navigation systems or page layouts
- Writing or reviewing content
- Conducting code reviews
- Performing accessibility audits
- Setting up automated testing pipelines
- Training team members on accessibility

**Key Philosophy:** Use this skill at the beginning of development, not as a debugging tool after problems arise.

## What This Skill Provides

### 1. Compliance Frameworks
- **WCAG 2.1 Level AA** (minimum requirement)
- **WCAG 2.1 Level AAA** (enhanced standards where feasible)
- **UK Public Sector Regulations** alignment
- **University of Sheffield specific requirements**

### 2. Development Guidance
- Semantic HTML patterns and best practices
- ARIA usage decision trees and implementation examples
- Keyboard navigation and focus management strategies
- Screen reader optimization techniques
- Form accessibility with comprehensive error handling
- Common accessible component patterns (modals, tabs, tables, forms)

### 3. Content Creation Standards
- Alternative text decision matrices and examples
- Video captioning and transcript requirements
- Heading hierarchy and document structure
- Link text and navigation guidance
- Plain English and University tone of voice alignment
- Multimedia accessibility workflows

### 4. Testing & Validation
- Automated testing integration (axe DevTools, WAVE, Pa11y)
- CI/CD pipeline configuration examples
- Manual testing protocols for keyboard and screen readers
- User testing strategies with assistive technology users
- Regular testing cadence recommendations

### 5. Design Standards
- Color contrast requirements and testing tools
- User preference support (prefers-reduced-motion, prefers-color-scheme)
- Responsive design and zoom requirements
- Touch target sizing and mobile accessibility
- Focus indicator design

### 6. Templates & Checklists
- Accessibility acceptance criteria for user stories
- Content accessibility review checklist
- WCAG 2.1 AA/AAA quick reference
- Component testing checklists
- Audit and remediation templates

## Sources and Standards

This skill was developed using the following authoritative sources:

### Primary Standards Documents

1. **Web Content Accessibility Guidelines (WCAG) 2.1**
   - Source: W3C Web Accessibility Initiative
   - URL: https://www.w3.org/TR/WCAG21/
   - Coverage: Complete Level A, AA, and AAA criteria
   - Implementation: All criteria mapped to practical examples

2. **University of Sheffield Content Accessibility Guidance**
   - Internal institutional document
   - Defines UoS-specific requirements and tone of voice
   - Includes multimedia standards and Kaltura workflows
   - Specifies diversity and inclusion considerations

3. **UK Government Service Manual**
   - Source: UK Government Digital Service (GDS)
   - URL: https://www.gov.uk/service-manual/helping-people-to-use-your-service/understanding-wcag
   - Provides practical guidance for implementing WCAG in UK public sector

4. **UK Public Sector Accessibility Requirements**
   - Source: UK Government
   - URL: https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps
   - Legal framework for public sector digital accessibility

5. **The A11y Project Checklist**
   - Source: The A11y Project community initiative
   - URL: https://www.a11yproject.com/checklist/
   - Practical accessibility checklist for web developers

### Technical Resources

6. **Accessibility Specialist Subagent Pattern**
   - Internal system design document
   - Defines proactive accessibility implementation approach
   - Emphasizes semantic HTML first, ARIA when necessary
   - Includes automated testing and CI/CD integration patterns

7. **Building Claude Skills: A Comprehensive Guide**
   - Internal skill development framework
   - Methodology for encoding expertise into reusable skills
   - Template structure and best practices

### Testing Tools Referenced

- **axe DevTools** (Deque Systems): Primary automated testing tool
- **WAVE** (WebAIM): Visual accessibility evaluation
- **Pa11y**: Command-line accessibility testing for CI/CD
- **Lighthouse** (Google): Built-in Chrome DevTools auditing
- **WebAIM Contrast Checker**: Color contrast validation

### Screen Reader Technologies

- **NVDA** (NonVisual Desktop Access): Free, open-source Windows screen reader
- **JAWS** (Freedom Scientific): Commercial Windows screen reader
- **VoiceOver** (Apple): Built-in macOS and iOS screen reader
- **TalkBack** (Google): Built-in Android screen reader

## Skill Structure

The skill is organized into the following major sections:

1. **Purpose Statement** - What this skill is for and who uses it
2. **Core Principles** - Fundamental accessibility philosophy
3. **Mental Model** - Framework for thinking about accessibility
4. **Process Documentation** - Phase-by-phase development workflow
5. **Templates & Tools** - Reusable checklists and reference materials
6. **Decision Heuristics** - When to use specific approaches
7. **Common Patterns** - Code examples for accessible components
8. **Screen Reader Optimization** - Detailed guidance for assistive technology support
9. **Reference Material** - WCAG criteria, external resources, UoS requirements
10. **Common Pitfalls** - Problems to avoid with solutions
11. **Implementation Workflow** - How to integrate into existing processes
12. **Success Metrics** - How to measure accessibility effectiveness

## Key Features

### Proactive Design
Unlike reactive accessibility remediation, this skill is designed to be invoked **before and during** development, preventing issues rather than fixing them.

### Semantic HTML First
Emphasizes using native HTML elements before reaching for ARIA, following web standards and best practices.

### Multi-Level Testing
Combines automated testing (catching ~30% of issues) with essential manual testing (catching the remaining ~70%) and user validation.

### Screen Reader Compatibility
Ensures compatibility with NVDA, JAWS, and VoiceOver through comprehensive testing guidance and optimization patterns.

### CI/CD Integration
Provides complete examples for integrating accessibility testing into continuous integration pipelines using Jest, Pa11y, and GitHub Actions/GitLab CI.

### User Preference Support
Respects user preferences including `prefers-reduced-motion` and `prefers-color-scheme` for enhanced user experience.

### AAA Enhancements
While AA is the minimum requirement, the skill identifies AAA criteria that align with UoS standards and significantly improve user experience (enhanced contrast, larger touch targets, clearer link text).

## Usage Examples

### Scenario 1: Building a New Component
```
I'm building a course registration form with conditional fields and validation.
Use the UoS accessibility framework to guide implementation.
Include: form labels, error handling, keyboard navigation, and ARIA attributes.
```

### Scenario 2: Code Review
```
Review this modal dialog component for accessibility compliance:
[paste code]

Check against WCAG 2.1 AA standards and UoS requirements.
Focus on: focus traps, keyboard handling, screen reader announcements.
```

### Scenario 3: Content Review
```
Review this department landing page for accessibility:
[paste content]

Check: heading hierarchy, link text, alt text, color contrast, Plain English.
Provide specific fixes for any issues found.
```

### Scenario 4: Planning New Features
```
I need to build a data visualization dashboard for research metrics.
Use the accessibility framework to define requirements before design begins.
Include: keyboard navigation, screen reader data tables, color contrast for charts.
```

### Scenario 5: Setting Up Testing
```
Help me configure accessibility testing in our CI/CD pipeline.
We use GitHub Actions and Jest for testing.
Include: axe-core integration, Pa11y setup, and automated Lighthouse audits.
```

## Compliance Scope

### Minimum Requirements (MUST)
- **WCAG 2.1 Level AA** across all University of Sheffield digital platforms
- **UK Public Sector Regulations** for websites and apps
- **Accessibility Statement** published and maintained
- **Regular Audits** conducted quarterly minimum

### Enhanced Standards (SHOULD)
- **WCAG 2.1 Level AAA** where feasible:
  - Enhanced contrast (7:1 for text)
  - Larger touch targets (44×44 CSS pixels)
  - Clearer link text (understandable out of context)
  - Animation controls (respect prefers-reduced-motion)
  - Plain English (already UoS standard)

### Testing Requirements
- **Automated Testing**: Every commit via CI/CD pipeline
- **Manual Testing**: Every sprint/release cycle
- **Screen Reader Testing**: All major releases with NVDA, JAWS, VoiceOver
- **User Testing**: Quarterly with assistive technology users
- **External Audit**: Annual review by certified accessibility auditor

## Integration with University Standards

This skill incorporates University of Sheffield specific requirements:

- **Kaltura** for video hosting and captioning
- **Plain English** and active voice in content
- **Sentence case** for headings (not title case or block capitals)
- **Diversity and inclusion** in multimedia representation
- **Short paragraphs** for scannable content
- **Tone of voice** alignment with university brand guidelines

## Limitations and Scope

### What This Skill Covers
- Web applications and digital platforms
- Content creation and multimedia
- UI components and interactive elements
- Testing and validation strategies
- WCAG 2.1 compliance (A, AA, AAA)

### What This Skill Does Not Cover
- Physical accessibility of buildings or spaces
- Assistive technology product selection
- Legal advice on compliance disputes
- Accessibility of third-party vendor products
- Document accessibility for formats other than web/HTML (though PDF guidance is included)

### Important Notes
- Automated tools catch only ~30% of accessibility issues; manual and user testing are essential
- Accessibility is an ongoing process, not a one-time checklist
- User feedback from people with disabilities is invaluable for validation
- When in doubt, test with real assistive technology users

## Contributing and Feedback

This skill is designed to evolve based on:
- Changes to WCAG standards
- Updates to University of Sheffield policies
- New testing tools and techniques
- User feedback from development teams
- Lessons learned from accessibility audits
- Emerging best practices in the field

Teams using this skill are encouraged to:
- Document accessibility issues and solutions
- Share successful patterns and implementations
- Report gaps or areas needing clarification
- Suggest improvements based on real-world usage

## Getting Started

1. **Review the complete skill document** to understand the full scope
2. **Bookmark key reference sections** (WCAG quick reference, checklists, common patterns)
3. **Set up automated testing** in your CI/CD pipeline using the provided examples
4. **Train your team** on when and how to invoke the skill
5. **Start using proactively** from the beginning of your next project
6. **Test with real users** who use assistive technologies
7. **Iterate and improve** based on feedback and audit results

## Additional Resources

### Official Documentation
- W3C WCAG 2.1: https://www.w3.org/TR/WCAG21/
- W3C WAI Tutorials: https://www.w3.org/WAI/tutorials/
- UK Government Service Manual: https://www.gov.uk/service-manual/helping-people-to-use-your-service/understanding-wcag

### Learning Resources
- WebAIM: https://webaim.org/
- The A11y Project: https://www.a11yproject.com/
- Deque University: https://dequeuniversity.com/
- MDN Accessibility: https://developer.mozilla.org/en-US/docs/Web/Accessibility

### Testing Tools
- axe DevTools: Browser extension for automated testing
- WAVE: https://wave.webaim.org/
- Pa11y: https://pa11y.org/
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/

### Screen Readers
- NVDA (Free, Windows): https://www.nvaccess.org/
- JAWS (Commercial, Windows): https://www.freedomscientific.com/products/software/jaws/
- VoiceOver (Built-in, Mac/iOS): System Preferences → Accessibility
- TalkBack (Built-in, Android): Settings → Accessibility
