---
name: accessible-web-development
description: "Build web applications that comply with University of Sheffield accessibility policies and WCAG 2.1 AA standards"
version: 0.1.0
domain: web-development, accessibility, compliance
---

# University of Sheffield Web Accessibility Skill

## Purpose Statement

This skill provides a structured approach to building web applications, content, and digital platforms that meet University of Sheffield accessibility requirements and WCAG 2.1 AA compliance standards.

**Target Users:** Web developers, product owners, content creators, UX designers, and communications specialists at the University of Sheffield

**Problems Solved:**
- Ensuring consistent accessibility compliance across all digital platforms
- Reducing remediation costs by building accessibility in from the start
- Meeting legal requirements for public sector websites and apps
- Creating inclusive experiences for all users regardless of ability

## Core Principle

**Accessibility is everyone's responsibility** - from developers to product owners to content specialists. The goal is to make all platforms, services, and content as accessible, inclusive, and usable as possible to all users.

## Mental Model: The Accessibility-First Framework

Think of accessibility as a series of checkpoints throughout the development lifecycle:

```
Planning → Design → Development → Content → Testing → Maintenance
    ↓         ↓          ↓           ↓         ↓          ↓
  Requirements  Visual    Semantic   Alt text  Audit   Continuous
  Definition    Design    HTML/ARIA  Captions  Tools   Monitoring
```

### Key Compliance Requirement
All University of Sheffield digital platforms must meet **WCAG 2.1 Level AA** standards across websites, apps, and other digital platforms.

---

## Process Documentation

### Phase 1: Planning & Requirements

**Step 1: Define Accessibility Requirements**
1. Identify content types (text, images, video, audio, interactive elements)
2. Determine target WCAG level (minimum: AA for UoS)
3. List assistive technologies to support (screen readers, keyboard navigation, voice control)
4. Document any exceptions with clear justification

**Step 2: Establish Responsibility Matrix**
- Developers: Semantic HTML, ARIA, keyboard navigation, focus management
- Designers: Color contrast, visual hierarchy, clear labeling
- Content creators: Alt text, captions, transcripts, plain English
- Product owners: Acceptance criteria, testing requirements, remediation budget

### Phase 2: Design & Visual Standards

**Color & Contrast Decision Tree**
```
For all text content:
├─ Standard text (< 18pt or < 14pt bold)?
│  └─ Minimum contrast: 4.5:1 against background
└─ Large text (≥ 18pt or ≥ 14pt bold)?
   └─ Minimum contrast: 3:0:1 against background

For non-text elements (icons, charts, UI components):
└─ Minimum contrast: 3:1 against adjacent colors
```

**Design Checklist:**
- [ ] Text contrast meets minimum ratios (use WebAIM Contrast Checker)
- [ ] Color is not the only differentiator (add patterns, labels, or icons)
- [ ] Instructions don't rely on sensory characteristics ("blue button" → "Submit button")
- [ ] Significant text is not embedded in images
- [ ] Font sizes support readability (minimum 16px for body text)
- [ ] Interactive elements have clear focus indicators
- [ ] Touch targets are minimum 44×44 CSS pixels

**When to Avoid Text in Images:**
❌ Never use for:
- Body content or instructions
- Navigation elements
- Data tables or statistics
- Social media quote graphics (UoS moved away from these)

✅ Acceptable for:
- Logos and branding (provide alt text)
- Decorative graphics where text is also available separately
- Screenshots with accompanying text alternative

### Phase 3: Development Standards

**Semantic HTML Framework**

Always use semantic HTML elements for their intended purpose:

```html
<!-- Good: Semantic structure -->
<header>
  <nav aria-label="Main navigation">
    <ul>
      <li><a href="/research">Research</a></li>
    </ul>
  </nav>
</header>

<main>
  <article>
    <h1>Page Title</h1>
    <section>
      <h2>Section Heading</h2>
      <p>Content...</p>
    </section>
  </article>
</main>

<footer>
  <!-- Footer content -->
</footer>

<!-- Bad: Non-semantic divs -->
<div class="header">
  <div class="nav">...</div>
</div>
```

**Heading Hierarchy Rules**
1. One `<h1>` per page (page title/topic)
2. Never skip heading levels (h1 → h2 → h3, not h1 → h3)
3. Headings indicate topic/purpose of content
4. Use headings for structure, not styling

**Link Purpose Standards**
```html
<!-- Bad: Ambiguous link text -->
<a href="/report.pdf">Click here</a>
<a href="/research">Read more</a>

<!-- Good: Descriptive link text -->
<a href="/report.pdf">Annual Research Report 2024 (PDF, 2.3MB)</a>
<a href="/research">Read more about quantum computing research</a>

<!-- Good: Context from surrounding content -->
<p>Our latest research explores quantum computing applications.</p>
<a href="/quantum-research">Learn more</a>
```

**Form Accessibility Pattern**
```html
<form>
  <!-- Always associate labels with inputs -->
  <label for="email">Email address</label>
  <input 
    type="email" 
    id="email" 
    name="email"
    required
    aria-describedby="email-help"
    autocomplete="email"
  >
  <span id="email-help">We'll never share your email</span>
  
  <!-- Error messaging -->
  <span id="email-error" role="alert" aria-live="polite">
    <!-- Error appears here when validation fails -->
  </span>
  
  <!-- Group related fields -->
  <fieldset>
    <legend>Contact preferences</legend>
    <input type="checkbox" id="newsletter" name="newsletter">
    <label for="newsletter">Receive newsletter</label>
  </fieldset>
  
  <button type="submit">Submit form</button>
</form>
```

**Keyboard Navigation Requirements**
- All interactive elements must be keyboard accessible (Tab, Enter, Space, Arrow keys)
- Focus order must be logical (follows visual layout)
- Focus must be visible at all times (clear focus indicator)
- No keyboard traps (users can Tab out of all components)
- Skip links for main content navigation

**ARIA Usage Guidelines**

When to use ARIA:
- Native HTML doesn't provide needed semantics
- Complex widgets (tabs, accordions, modals)
- Dynamic content updates (live regions)
- Custom interactive components

ARIA First Rule: **Don't use ARIA if HTML provides native semantics**

```html
<!-- Bad: Unnecessary ARIA -->
<div role="button" tabindex="0" onclick="...">Click me</div>

<!-- Good: Native HTML -->
<button type="button">Click me</button>

<!-- Good: ARIA for custom widget -->
<div role="tablist">
  <button role="tab" aria-selected="true" aria-controls="panel1">Tab 1</button>
  <button role="tab" aria-selected="false" aria-controls="panel2">Tab 2</button>
</div>
<div role="tabpanel" id="panel1">Content 1</div>
```

### Phase 4: Content Creation Standards

**Alternative Text Framework**

Decision tree for alt text:
```
Is the image meaningful?
├─ YES: Does it convey information not in surrounding text?
│  ├─ YES: Write descriptive alt text (what would you tell someone over phone?)
│  └─ NO: Use alt="" (decorative/redundant)
└─ NO: Use alt="" (purely decorative)

Special cases:
├─ Complex images (charts, diagrams): alt text + long description
├─ Functional images (buttons, links): Describe function, not appearance
└─ Images of text: Include the text in alt attribute
```

**Alt Text Quality Standards:**
- Describe content and function, not appearance
- Keep concise (aim for under 150 characters when possible)
- Don't start with "image of" or "picture of"
- Include text that appears in the image
- For complex images, provide both brief alt text and detailed description

**Examples:**
```html
<!-- Decorative image -->
<img src="decorative-border.png" alt="">

<!-- Informative image -->
<img src="campus-map.jpg" alt="University of Sheffield campus map showing Arts Tower, Diamond, and Students' Union locations">

<!-- Functional image (button) -->
<a href="/search">
  <img src="search-icon.svg" alt="Search">
</a>

<!-- Complex chart -->
<img 
  src="enrollment-chart.png" 
  alt="Bar chart showing student enrollment trends 2020-2024"
  aria-describedby="chart-details"
>
<div id="chart-details">
  Enrollment increased from 28,000 in 2020 to 32,000 in 2024, 
  with largest growth in Engineering (15%) and Medicine (12%).
</div>
```

**Social Media Alt Text:**
Apply same standards across all platforms:
- Twitter/X: Set image descriptions
- Instagram: Add alt text to posts
- Facebook: Include image descriptions
- LinkedIn: Use alt text feature

### Phase 5: Multimedia Accessibility

**Video Content Requirements**

All video content must have:
1. **Captions/Subtitles** (synchronized with audio)
2. **Transcript** (full text version)
3. **Audio Description** (for instructional/informational videos)

**Caption Standards:**
- Upload as SRT file (not burned into video)
- Supported platforms: YouTube, Kaltura, Facebook, Twitter
- Include speaker identification
- Describe relevant sound effects [applause], [music playing]
- Accurate spelling and punctuation
- Tool: Kaltura's captioning software for UoS content

**Transcript Template:**
```
[Video Title]
Duration: [X minutes]

Speakers: [List names and roles]

[00:00:00] - SPEAKER NAME
Transcript text here...

[00:00:15] - SPEAKER NAME
Next section of dialogue...

[Visual descriptions in brackets when needed]
[Shows graph of enrollment data]

[00:01:30] - [Background music plays]
...
```

**Audio Description Guidelines:**
- Describe visual elements not evident from audio
- Insert during natural pauses in dialogue
- Focus on actions, settings, body language, on-screen text
- Required for: instructional videos, demos, visual storytelling

**Audio-Only Content (Podcasts):**
- Provide full transcript
- Include speaker identification
- Describe relevant non-speech sounds
- Publish alongside audio file

**Live Video Streaming:**
- Enable live captions (YouTube, Kaltura auto-captioning)
- Note: Quality depends on platform capabilities
- Provide transcript post-event when possible

### Phase 6: Testing & Validation

**Multi-Level Testing Approach**

**Level 1: Automated Testing (Baseline)**
Tools:
- WAVE (WebAIM): Browser extension for page analysis
- axe DevTools: Comprehensive accessibility testing
- Lighthouse: Built into Chrome DevTools
- Pa11y: Command-line testing tool

Run on:
- Every page template
- Dynamic states (modals, menus, forms with errors)
- Representative content pages

**Level 2: Manual Testing (Essential)**
- Keyboard-only navigation (disconnect mouse, use Tab, Enter, Space, Arrows)
- Screen reader testing (NVDA on Windows, VoiceOver on Mac)
- Color contrast verification (WebAIM Contrast Checker)
- Zoom to 200% (content must remain readable and functional)
- Mobile screen reader testing (TalkBack on Android, VoiceOver on iOS)

**Level 3: User Testing (Validation)**
- Test with actual users who use assistive technologies
- Observe task completion and pain points
- Gather feedback on usability, not just technical compliance

**Testing Checklist by Component:**

Forms:
- [ ] All inputs have associated labels
- [ ] Required fields are indicated
- [ ] Error messages are clear and associated with fields
- [ ] Success/error states announced to screen readers
- [ ] Can complete entire form with keyboard only
- [ ] Autocomplete attributes for common fields

Navigation:
- [ ] Skip to main content link present
- [ ] Logical tab order
- [ ] Current page indicated in navigation
- [ ] Dropdown menus keyboard accessible
- [ ] Breadcrumbs present where appropriate

Interactive Components:
- [ ] All states keyboard accessible
- [ ] Focus indicators visible
- [ ] ARIA states update appropriately
- [ ] Screen reader announces state changes
- [ ] No keyboard traps

---

## Templates & Tools

### 1. Accessibility Acceptance Criteria Template

```markdown
## User Story
As a [user type], I want to [action] so that [benefit]

## Accessibility Acceptance Criteria

### Keyboard
- [ ] All functionality available via keyboard
- [ ] Logical tab order
- [ ] Visible focus indicators
- [ ] No keyboard traps

### Screen Reader
- [ ] All content announced appropriately
- [ ] Form labels associated correctly
- [ ] Headings provide clear structure
- [ ] Link purpose clear from link text
- [ ] Dynamic updates announced (ARIA live regions)

### Visual
- [ ] Color contrast meets WCAG AA (4.5:1 for text)
- [ ] Content readable at 200% zoom
- [ ] No information conveyed by color alone
- [ ] Focus indicators visible

### Content
- [ ] Page has descriptive, unique title
- [ ] Headings follow logical hierarchy
- [ ] Alt text provided for meaningful images
- [ ] Captions provided for video content
- [ ] Link text is descriptive

### Testing
- [ ] Passes automated testing (WAVE, axe)
- [ ] Passes keyboard-only testing
- [ ] Passes screen reader testing (NVDA/VoiceOver)
```

### 2. Content Accessibility Checklist

```markdown
# Content Accessibility Review Checklist

## Text Content
- [ ] Page has unique, descriptive title
- [ ] Headings used for structure (not styling)
- [ ] Heading hierarchy is logical (no skipped levels)
- [ ] Paragraphs are short and scannable
- [ ] Sentence case used (not block capitals/title case)
- [ ] Plain English used (jargon avoided)
- [ ] Active voice preferred over passive
- [ ] University tone of voice maintained

## Links
- [ ] Link text describes destination/purpose
- [ ] No "click here" or "read more" without context
- [ ] External links indicated
- [ ] PDF links include format and file size
  Example: "Annual Report (PDF, 2.3MB)"

## Images
- [ ] All images have alt text or alt=""
- [ ] Alt text describes content/function
- [ ] Complex images have detailed descriptions
- [ ] No significant text embedded in images
- [ ] Decorative images use alt=""

## Color & Design
- [ ] Text contrast ratio minimum 4.5:1
- [ ] Color not sole means of conveying information
- [ ] Instructions don't rely on sensory characteristics
- [ ] Content readable without CSS

## Multimedia
- [ ] Videos have synchronized captions (SRT file)
- [ ] Videos have transcripts
- [ ] Instructional videos have audio descriptions
- [ ] Audio-only content has transcripts
- [ ] Podcasts have transcripts with speaker IDs

## Social Media
- [ ] Images have alt text/descriptions
- [ ] Videos have captions
- [ ] Diverse representation in imagery
- [ ] No reliance on text-in-image graphics
```

### 3. WCAG 2.1 AA Quick Reference

```markdown
# WCAG 2.1 AA Requirements - Quick Reference

## Level A (Must Have)

### Perceivable
1.1.1 - Non-text content has text alternatives
1.2.1 - Audio-only/video-only has alternatives
1.2.2 - Captions for pre-recorded video
1.2.3 - Audio description OR transcript for video
1.3.1 - Info/structure can be programmatically determined
1.3.2 - Meaningful sequence preserved
1.3.3 - Instructions don't rely solely on sensory characteristics
1.4.1 - Color not sole means of conveying information
1.4.2 - Audio controls available

### Operable
2.1.1 - Keyboard accessible
2.1.2 - No keyboard trap
2.1.4 - Single character shortcuts can be remapped
2.2.1 - Timing adjustable
2.2.2 - Pause/stop/hide for moving content
2.3.1 - No flashing more than 3 times per second
2.4.1 - Skip blocks mechanism (skip links)
2.4.2 - Pages have titles
2.4.3 - Logical focus order
2.4.4 - Link purpose clear from text/context
2.5.1 - Pointer gestures have alternatives
2.5.2 - Pointer cancellation possible
2.5.3 - Label in name matches visible label
2.5.4 - Motion actuation can be disabled

### Understandable
3.1.1 - Page language identified
3.2.1 - Focus doesn't trigger unexpected changes
3.2.2 - Input doesn't trigger unexpected changes
3.3.1 - Errors identified
3.3.2 - Labels or instructions provided

### Robust
4.1.1 - Valid HTML parsing
4.1.2 - Name, role, value for UI components
4.1.3 - Status messages programmatically determined

## Level AA (UoS Requirement)

### Perceivable
1.2.4 - Captions for live video
1.2.5 - Audio description for pre-recorded video
1.3.4 - Orientation not restricted
1.3.5 - Input purpose can be programmatically determined
1.4.3 - Contrast ratio minimum 4.5:1 (3:1 for large text)
1.4.4 - Text can be resized to 200%
1.4.5 - Images of text avoided
1.4.10 - Reflow at 400% zoom
1.4.11 - Non-text contrast minimum 3:1
1.4.12 - Text spacing adjustable
1.4.13 - Content on hover/focus dismissable and persistent

### Operable
2.4.5 - Multiple ways to find pages
2.4.6 - Headings and labels descriptive
2.4.7 - Focus visible

### Understandable
3.1.2 - Language of parts identified
3.2.3 - Consistent navigation
3.2.4 - Consistent identification
3.3.3 - Error suggestions provided
3.3.4 - Error prevention for legal/financial/data
```

### 4. Alt Text Decision Matrix

| Image Type | Alt Text Approach | Example |
|------------|-------------------|---------|
| Informative photo | Describe key information | "Students working in the Diamond building's collaborative learning space" |
| Decorative image | Use alt="" | `<img src="border.png" alt="">` |
| Functional image | Describe function | "Search" (for search icon button) |
| Complex diagram | Brief alt + long description | alt="Process diagram for student enrollment" + detailed description below |
| Image of text | Include all text | "Welcome to the University of Sheffield" |
| Logo | Include organization name | "University of Sheffield logo" |
| Chart/graph | Brief alt + data table | alt="Bar chart of enrollment trends" + full data table |
| Linked image | Describe link destination | "View campus map (opens in new window)" |

### 5. Color Contrast Testing Reference

**Tools:**
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- Chrome DevTools: Inspect element → Accessibility pane
- Figma plugins: Stark, Contrast

**Common Issues & Fixes:**

| Problem | Ratio | Solution |
|---------|-------|----------|
| Light gray text (#767676) on white | 4.5:1 | ✓ Passes for normal text |
| Light gray text (#999999) on white | 2.8:1 | ✗ Fails - darken to #767676 or darker |
| White text on UoS blue (#00AEEF) | 2.3:1 | ✗ Fails - use darker blue (#0077C8) |
| Black text on light yellow (#FFF8DC) | 18:1 | ✓ Passes with excellent contrast |

**UoS Brand Colors - Accessible Combinations:**
- White text on UoS blue (#009ADE): 3.2:1 ✗ Fails for normal text
- Black text on UoS yellow (#FECB00): 10:1 ✓ Passes
- Solution: Use UoS blue for large headings only, or darken for body text

---

## Decision Heuristics

### When to Use ARIA vs Native HTML

**Decision Flow:**
```
Need interactive element?
├─ Native HTML exists (button, input, select)?
│  └─ ✓ Use native HTML (no ARIA needed)
└─ No native equivalent?
   ├─ Can I restructure to use native HTML?
   │  └─ ✓ Restructure (preferred)
   └─ Must use custom widget?
      └─ ✓ Use ARIA + keyboard handling + focus management
```

**Examples:**
- Button → Use `<button>`, not `<div role="button">`
- Checkbox → Use `<input type="checkbox">`, not `<div role="checkbox">`
- Radio group → Use `<input type="radio">` with `<fieldset>`, not ARIA radio
- Tabs → No native HTML, use ARIA tablist pattern
- Modal dialog → No native HTML, use ARIA dialog pattern

### Image Description: Brief vs Detailed

**Use Brief Alt Text When:**
- Image is simple with single clear message
- Context provided in surrounding text
- User doesn't need comprehensive details

**Use Detailed Description When:**
- Image contains multiple data points (charts, graphs)
- Process diagram with multiple steps
- Map with multiple locations
- Infographic with layered information

**Provide Both:**
- Brief alt: "Bar chart showing enrollment growth 2020-2024"
- Detailed description: Full data values, trends, and insights

### Video Caption vs Audio Description

**Captions are for:**
- Dialogue and speech
- Speaker identification
- Sound effects relevant to content
- Music cues when relevant

**Audio Descriptions are for:**
- Visual information not evident from audio alone
- On-screen text not read aloud
- Actions, expressions, scene changes
- Demonstrations and visual instructions

**When you need both:**
- Instructional videos (showing how to do something)
- Narrative content with visual storytelling
- Scientific demonstrations
- Product demonstrations

---

## Common Accessibility Patterns

### Accessible Modal Dialog

```html
<div role="dialog" 
     aria-modal="true" 
     aria-labelledby="dialog-title"
     aria-describedby="dialog-description">
  
  <h2 id="dialog-title">Confirm Submission</h2>
  <p id="dialog-description">
    Are you sure you want to submit this form?
  </p>
  
  <button type="button" onclick="confirmAction()">
    Confirm
  </button>
  <button type="button" onclick="closeDialog()">
    Cancel
  </button>
</div>

<!-- JavaScript requirements: -->
<!-- - Focus trap within modal -->
<!-- - Close on Escape key -->
<!-- - Return focus to trigger when closed -->
<!-- - Prevent background scroll -->
```

### Accessible Tabs

```html
<div class="tabs">
  <div role="tablist" aria-label="Course information">
    <button role="tab" 
            aria-selected="true" 
            aria-controls="overview-panel"
            id="overview-tab"
            tabindex="0">
      Overview
    </button>
    <button role="tab" 
            aria-selected="false" 
            aria-controls="modules-panel"
            id="modules-tab"
            tabindex="-1">
      Modules
    </button>
  </div>
  
  <div role="tabpanel" 
       id="overview-panel"
       aria-labelledby="overview-tab"
       tabindex="0">
    <!-- Overview content -->
  </div>
  
  <div role="tabpanel" 
       id="modules-panel"
       aria-labelledby="modules-tab"
       tabindex="0"
       hidden>
    <!-- Modules content -->
  </div>
</div>

<!-- Keyboard: -->
<!-- - Tab: Move focus into and out of tab list -->
<!-- - Left/Right Arrow: Navigate between tabs -->
<!-- - Home/End: First/last tab -->
<!-- - Space/Enter: Activate tab -->
```

### Accessible Form Validation

```html
<form novalidate>
  <div class="form-field">
    <label for="email">Email address *</label>
    <input 
      type="email" 
      id="email" 
      name="email"
      required
      aria-required="true"
      aria-invalid="false"
      aria-describedby="email-help email-error"
    >
    <span id="email-help" class="help-text">
      We'll use this to contact you about your application
    </span>
    <span id="email-error" class="error-message" role="alert" aria-live="polite">
      <!-- Error message inserted here on validation -->
    </span>
  </div>
  
  <button type="submit">Submit application</button>
</form>

<!-- On validation error: -->
<!-- 1. Set aria-invalid="true" on input -->
<!-- 2. Insert error message in error span -->
<!-- 3. Move focus to first error -->
<!-- 4. Announce error count (e.g., "3 errors found") -->
```

### Accessible Data Table

```html
<table>
  <caption>Student enrollment by department, 2024</caption>
  <thead>
    <tr>
      <th scope="col">Department</th>
      <th scope="col">Undergraduate</th>
      <th scope="col">Postgraduate</th>
      <th scope="col">Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Engineering</th>
      <td>1,245</td>
      <td>567</td>
      <td>1,812</td>
    </tr>
    <tr>
      <th scope="row">Medicine</th>
      <td>890</td>
      <td>432</td>
      <td>1,322</td>
    </tr>
  </tbody>
</table>
```

---

## Reference Material

### University of Sheffield Specific Requirements

**Mandatory Compliance:**
- WCAG 2.1 Level AA across all platforms
- Public sector accessibility regulations
- Accessibility statement required on website

**Responsibility:**
- Everyone's responsibility (not just developers)
- Standards apply unless clear reason why not possible
- Must document any exceptions with justification

**Tone of Voice:**
- Active voice over passive
- Plain English (avoid jargon)
- Short paragraphs for scannability
- Sentence case (not title case or capitals)

**Diversity & Inclusion:**
- Videos must reflect diverse community
- Conscious representation across communications
- Broad mix across all content

**Platform-Specific:**
- Kaltura for video hosting and captioning
- YouTube for public video content
- Standard SRT format for captions
- University accessibility statement template

### External Resources

**Official Guidelines:**
- WCAG 2.1: https://www.w3.org/TR/WCAG21/
- UK Government Service Manual: https://www.gov.uk/service-manual/helping-people-to-use-your-service/understanding-wcag
- UK Public Sector Requirements: https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps

**Testing Tools:**
- WAVE: https://wave.webaim.org/
- axe DevTools: Browser extension
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- A11y Project Checklist: https://www.a11yproject.com/checklist/

**Screen Readers:**
- NVDA (Windows): Free, widely used
- JAWS (Windows): Commercial, enterprise standard
- VoiceOver (Mac/iOS): Built-in
- TalkBack (Android): Built-in

**Learning Resources:**
- WebAIM: https://webaim.org/
- A11y Project: https://www.a11yproject.com/
- Deque University: https://dequeuniversity.com/
- W3C WAI Tutorials: https://www.w3.org/WAI/tutorials/

---

## Common Pitfalls & Solutions

### Pitfall 1: Generic Link Text
**Problem:** "Click here" and "Read more" links don't make sense out of context

**Solution:**
```html
<!-- Bad -->
<a href="/research.pdf">Click here</a> to read our research report

<!-- Good -->
<a href="/research.pdf">Annual Research Report 2024 (PDF, 2.3MB)</a>
```

### Pitfall 2: Missing Form Labels
**Problem:** Placeholder text is not a label

**Solution:**
```html
<!-- Bad -->
<input type="text" placeholder="Email address">

<!-- Good -->
<label for="email">Email address</label>
<input type="email" id="email" placeholder="name@example.com">
```

### Pitfall 3: Div/Span Buttons
**Problem:** Using divs/spans as buttons breaks keyboard access and semantics

**Solution:**
```html
<!-- Bad -->
<div class="button" onclick="submit()">Submit</div>

<!-- Good -->
<button type="button" onclick="submit()">Submit</button>
```

### Pitfall 4: Low Color Contrast
**Problem:** Light gray text (#CCCCCC) on white fails WCAG

**Solution:**
- Test all color combinations
- Minimum 4.5:1 for normal text
- Minimum 3:1 for large text (18pt+)
- Use automated tools during design

### Pitfall 5: Auto-Playing Content
**Problem:** Videos/audio that auto-play interfere with screen readers

**Solution:**
```html
<!-- Add controls and no autoplay -->
<video controls>
  <source src="video.mp4" type="video/mp4">
  <track kind="captions" src="captions.vtt" srclang="en">
</video>
```

### Pitfall 6: PDF Accessibility
**Problem:** PDFs often inaccessible, no alt text, no logical structure

**Solution:**
- Prefer HTML content over PDF when possible
- If PDF required:
  - Create from accessible source (not scanned images)
  - Tag document structure properly
  - Add alt text to images
  - Ensure reading order is correct
  - Test with screen reader
  - Provide HTML alternative when possible

### Pitfall 7: Keyboard Traps
**Problem:** Users can Tab into component but can't Tab out

**Solution:**
- Test every interactive component with keyboard only
- Ensure Escape key closes modals/menus
- Use proper focus management
- Test roving tabindex patterns thoroughly

### Pitfall 8: Missing Page Titles
**Problem:** Generic or duplicate page titles don't help users orient

**Solution:**
```html
<!-- Bad -->
<title>University of Sheffield</title>

<!-- Good -->
<title>Computer Science MSc Programme - University of Sheffield</title>
<!-- Pattern: Specific page - Section - Site name -->
```

---

## Implementation Workflow

### For New Projects

1. **Requirements Phase**
   - Add accessibility acceptance criteria to all user stories
   - Include accessibility in definition of done
   - Budget for testing and remediation

2. **Design Phase**
   - Design with accessibility from start (not retrofitted)
   - Test color contrast in design tools
   - Plan heading hierarchy and page structure
   - Design focus states and keyboard interactions

3. **Development Phase**
   - Use semantic HTML first
   - Add ARIA only when necessary
   - Implement keyboard navigation
   - Test with screen readers during development

4. **Content Phase**
   - Write alt text for all images
   - Create captions for videos
   - Ensure link text is descriptive
   - Follow content guidelines

5. **Testing Phase**
   - Run automated tools (WAVE, axe)
   - Conduct keyboard-only testing
   - Test with screen readers
   - User testing with assistive technology users

6. **Launch & Maintain**
   - Publish accessibility statement
   - Monitor for issues
   - Regular audits
   - Update as content changes

### For Existing Projects

1. **Audit:** Use automated tools + manual testing
2. **Prioritize:** Critical issues first (keyboard access, contrast, alt text)
3. **Remediate:** Fix issues systematically
4. **Document:** Track issues and fixes
5. **Prevent:** Add accessibility to ongoing process

---

## How to Use This Skill

### Scenario 1: Building New Web Application
```
I'm building a student portal at University of Sheffield. 
Use the UoS accessibility framework to guide development.

Focus on: form accessibility, navigation patterns, and content structure.
```

### Scenario 2: Content Review
```
Review this page content for UoS accessibility compliance:
[paste content]

Check against WCAG 2.1 AA requirements and UoS content standards.
```

### Scenario 3: Component Development
```
I need to build an accessible modal dialog for course selection.
Use the UoS accessibility patterns and provide complete implementation.
```

### Scenario 4: Accessibility Audit
```
Audit this website section for accessibility issues:
[URL or description]

Use UoS compliance requirements and provide prioritized fix list.
```

---

## Success Metrics

**Technical Compliance:**
- 100% WCAG 2.1 AA compliance
- Zero critical accessibility errors in automated testing
- All pages pass keyboard-only navigation test
- All content announced correctly by screen readers

**User Experience:**
- Users with disabilities can complete all tasks
- Equivalent experience regardless of ability
- Positive feedback from assistive technology users
- No accessibility-related support tickets

**Process Integration:**
- Accessibility in acceptance criteria for all stories
- Accessibility testing in CI/CD pipeline
- Regular accessibility audits completed
- Team trained on accessibility standards

---

## Version History

**v1.0 (2024)** - Initial release
- WCAG 2.1 AA compliance framework
- University of Sheffield specific requirements
- Development patterns and templates
- Content creation guidelines
- Testing and validation processes
