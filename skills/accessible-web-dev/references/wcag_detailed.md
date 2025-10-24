# WCAG 2.1 Detailed Reference Guide

Complete reference for Web Content Accessibility Guidelines 2.1 Level A and AA requirements.

## Table of Contents

- [Principle 1: Perceivable](#principle-1-perceivable)
- [Principle 2: Operable](#principle-2-operable)
- [Principle 3: Understandable](#principle-3-understandable)
- [Principle 4: Robust](#principle-4-robust)

---

## Principle 1: Perceivable

Information and user interface components must be presentable to users in ways they can perceive.

### Guideline 1.1: Text Alternatives

Provide text alternatives for any non-text content.

#### 1.1.1 Non-text Content (Level A)

All non-text content that is presented to the user has a text alternative that serves the equivalent purpose, except for the situations listed below.

**Controls, Input:** If non-text content is a control or accepts user input, then it has a name that describes its purpose.

**Time-Based Media:** If non-text content is time-based media, then text alternatives at least provide descriptive identification of the non-text content.

**Test:** If non-text content is a test or exercise that would be invalid if presented in text, then text alternatives at least provide descriptive identification.

**Sensory:** If non-text content is primarily intended to create a specific sensory experience, then text alternatives at least provide descriptive identification.

**CAPTCHA:** If the purpose of non-text content is to confirm that content is being accessed by a person rather than a computer, then text alternatives that identify and describe the purpose of the non-text content are provided, and alternative forms of CAPTCHA using output modes for different types of sensory perception are provided.

**Decoration, Formatting, Invisible:** If non-text content is pure decoration, is used only for visual formatting, or is not presented to users, then it is implemented in a way that it can be ignored by assistive technology.

**Implementation:**
```html
<!-- Informative image -->
<img src="chart.png" alt="Bar chart showing 25% increase in enrollment">

<!-- Decorative image -->
<img src="decoration.png" alt="">

<!-- Functional image -->
<button>
  <img src="search.svg" alt="Search">
</button>

<!-- Complex image -->
<img src="complex-chart.png" alt="Sales data 2020-2024" aria-describedby="chart-desc">
<div id="chart-desc">
  Detailed description: Sales increased from $1M in 2020 to $1.5M in 2024...
</div>
```

### Guideline 1.2: Time-based Media

Provide alternatives for time-based media.

#### 1.2.1 Audio-only and Video-only (Prerecorded) (Level A)

For prerecorded audio-only and prerecorded video-only media:

**Audio-only:** An alternative for time-based media is provided that presents equivalent information.

**Video-only:** Either an alternative for time-based media or an audio track is provided that presents equivalent information.

#### 1.2.2 Captions (Prerecorded) (Level A)

Captions are provided for all prerecorded audio content in synchronized media, except when the media is a media alternative for text and is clearly labeled as such.

**Implementation:**
```html
<video controls>
  <source src="lecture.mp4" type="video/mp4">
  <track kind="captions" src="captions-en.vtt" srclang="en" label="English">
  <track kind="captions" src="captions-es.vtt" srclang="es" label="Español">
</video>
```

#### 1.2.3 Audio Description or Media Alternative (Prerecorded) (Level A)

An alternative for time-based media or audio description of the prerecorded video content is provided for synchronized media.

#### 1.2.4 Captions (Live) (Level AA)

Captions are provided for all live audio content in synchronized media.

#### 1.2.5 Audio Description (Prerecorded) (Level AA)

Audio description is provided for all prerecorded video content in synchronized media.

### Guideline 1.3: Adaptable

Create content that can be presented in different ways without losing information or structure.

#### 1.3.1 Info and Relationships (Level A)

Information, structure, and relationships conveyed through presentation can be programmatically determined or are available in text.

**Implementation:**
```html
<!-- Semantic structure -->
<article>
  <h1>Article Title</h1>
  <section>
    <h2>Section Heading</h2>
    <p>Content...</p>
  </section>
</article>

<!-- Form relationships -->
<label for="email">Email</label>
<input type="email" id="email" name="email">

<!-- Table relationships -->
<table>
  <caption>Student Enrollment Data</caption>
  <thead>
    <tr>
      <th scope="col">Year</th>
      <th scope="col">Students</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">2024</th>
      <td>32,000</td>
    </tr>
  </tbody>
</table>
```

#### 1.3.2 Meaningful Sequence (Level A)

When the sequence in which content is presented affects its meaning, a correct reading sequence can be programmatically determined.

#### 1.3.3 Sensory Characteristics (Level A)

Instructions provided for understanding and operating content do not rely solely on sensory characteristics of components such as shape, color, size, visual location, orientation, or sound.

**Bad:**
- "Click the green button to continue"
- "Fill out the form on the right"

**Good:**
- "Click the Submit button to continue"
- "Fill out the Contact Form below"

#### 1.3.4 Orientation (Level AA)

Content does not restrict its view and operation to a single display orientation, such as portrait or landscape, unless a specific display orientation is essential.

#### 1.3.5 Identify Input Purpose (Level AA)

The purpose of each input field collecting information about the user can be programmatically determined when:
- The input field serves a purpose identified in the Input Purposes for User Interface Components section
- The content is implemented using technologies with support for identifying the expected meaning for form input data

**Implementation:**
```html
<input type="text"
       name="name"
       autocomplete="name"
       id="name">

<input type="email"
       name="email"
       autocomplete="email"
       id="email">

<input type="tel"
       name="phone"
       autocomplete="tel"
       id="phone">
```

### Guideline 1.4: Distinguishable

Make it easier for users to see and hear content including separating foreground from background.

#### 1.4.1 Use of Color (Level A)

Color is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element.

**Bad:**
- Required fields indicated only by red color
- Chart legend using only colors to differentiate data

**Good:**
- Required fields indicated by asterisk (*) AND red color
- Chart legend using colors + patterns + labels

#### 1.4.2 Audio Control (Level A)

If any audio on a Web page plays automatically for more than 3 seconds, either a mechanism is available to pause or stop the audio, or a mechanism is available to control audio volume independently from the overall system volume level.

#### 1.4.3 Contrast (Minimum) (Level AA)

The visual presentation of text and images of text has a contrast ratio of at least 4.5:1, except:

**Large Text:** Large-scale text and images of large-scale text have a contrast ratio of at least 3:1.
- Large text: 18pt (24px) or larger, or 14pt (18.5px) bold or larger

**Incidental:** Text or images of text that are part of an inactive user interface component, pure decoration, not visible, or part of a picture that contains significant other visual content, have no contrast requirement.

**Logotypes:** Text that is part of a logo or brand name has no contrast requirement.

**Testing:** Use WebAIM Contrast Checker or browser DevTools

#### 1.4.4 Resize Text (Level AA)

Except for captions and images of text, text can be resized without assistive technology up to 200 percent without loss of content or functionality.

**Testing:** Zoom browser to 200% and verify:
- All content is visible
- No horizontal scrolling required (for vertically scrolling content)
- Text doesn't overlap
- All functionality remains available

#### 1.4.5 Images of Text (Level AA)

If the technologies being used can achieve the visual presentation, text is used to convey information rather than images of text except:

**Customizable:** The image of text can be visually customized to the user's requirements.

**Essential:** A particular presentation of text is essential to the information being conveyed (logos, brand names).

#### 1.4.10 Reflow (Level AA)

Content can be presented without loss of information or functionality, and without requiring scrolling in two dimensions for:
- Vertical scrolling content at a width equivalent to 320 CSS pixels
- Horizontal scrolling content at a height equivalent to 256 CSS pixels

Except for parts of the content which require two-dimensional layout for usage or meaning.

**Testing:** Set browser width to 1280px, zoom to 400%

#### 1.4.11 Non-text Contrast (Level AA)

The visual presentation of User Interface Components and Graphical Objects has a contrast ratio of at least 3:1 against adjacent color(s):

**User Interface Components:** Visual information required to identify user interface components and states (except inactive components)

**Graphical Objects:** Parts of graphics required to understand the content (unless a particular presentation is essential)

**Examples:**
- Form input borders
- Focus indicators
- Icons that convey information
- Chart elements

#### 1.4.12 Text Spacing (Level AA)

No loss of content or functionality occurs by setting all of the following and by changing no other style property:
- Line height (line spacing) to at least 1.5 times the font size
- Spacing following paragraphs to at least 2 times the font size
- Letter spacing (tracking) to at least 0.12 times the font size
- Word spacing to at least 0.16 times the font size

#### 1.4.13 Content on Hover or Focus (Level AA)

Where receiving and then removing pointer hover or keyboard focus triggers additional content to become visible and then hidden, the following are true:

**Dismissible:** A mechanism is available to dismiss the additional content without moving pointer hover or keyboard focus

**Hoverable:** If pointer hover can trigger the additional content, then the pointer can be moved over the additional content without the additional content disappearing

**Persistent:** The additional content remains visible until the hover or focus trigger is removed, the user dismisses it, or its information is no longer valid

---

## Principle 2: Operable

User interface components and navigation must be operable.

### Guideline 2.1: Keyboard Accessible

Make all functionality available from a keyboard.

#### 2.1.1 Keyboard (Level A)

All functionality of the content is operable through a keyboard interface without requiring specific timings for individual keystrokes, except where the underlying function requires input that depends on the path of the user's movement and not just the endpoints.

**Testing:**
- Disconnect mouse
- Navigate using Tab, Shift+Tab, Enter, Space, Arrow keys
- Verify all interactive elements are reachable
- Verify all functionality can be completed

#### 2.1.2 No Keyboard Trap (Level A)

If keyboard focus can be moved to a component of the page using a keyboard interface, then focus can be moved away from that component using only a keyboard interface.

**Common issues:**
- Modal dialogs that don't allow Escape to close
- Custom widgets that trap Tab key
- Embedded content (iframes, plugins)

#### 2.1.4 Character Key Shortcuts (Level A)

If a keyboard shortcut is implemented in content using only letter (including upper- and lower-case letters), punctuation, number, or symbol characters, then at least one of the following is true:

**Turn off:** A mechanism is available to turn the shortcut off
**Remap:** A mechanism is available to remap the shortcut
**Active only on focus:** The keyboard shortcut is only active when component has focus

### Guideline 2.2: Enough Time

Provide users enough time to read and use content.

#### 2.2.1 Timing Adjustable (Level A)

For each time limit that is set by the content, at least one of the following is true:

**Turn off:** User can turn off time limit before encountering it
**Adjust:** User can adjust time limit before encountering it over a wide range (at least 10x)
**Extend:** User is warned before time expires and given at least 20 seconds to extend
**Real-time Exception:** Time limit is a required part of a real-time event
**Essential Exception:** Time limit is essential
**20 Hour Exception:** Time limit is longer than 20 hours

#### 2.2.2 Pause, Stop, Hide (Level A)

For moving, blinking, scrolling, or auto-updating information, all of the following are true:

**Moving, blinking, scrolling:** For any moving, blinking or scrolling information that:
- starts automatically
- lasts more than five seconds
- is presented in parallel with other content

there is a mechanism for the user to pause, stop, or hide it.

**Auto-updating:** For any auto-updating information that:
- starts automatically
- is presented in parallel with other content

there is a mechanism for the user to pause, stop, or hide it or to control the frequency of the update.

### Guideline 2.3: Seizures and Physical Reactions

Do not design content in a way that is known to cause seizures or physical reactions.

#### 2.3.1 Three Flashes or Below Threshold (Level A)

Web pages do not contain anything that flashes more than three times in any one second period, or the flash is below the general flash and red flash thresholds.

### Guideline 2.4: Navigable

Provide ways to help users navigate, find content, and determine where they are.

#### 2.4.1 Bypass Blocks (Level A)

A mechanism is available to bypass blocks of content that are repeated on multiple Web pages.

**Implementation:**
```html
<!-- Skip link -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<main id="main-content">
  <!-- Main content -->
</main>

<style>
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: #000;
  color: white;
  padding: 8px;
  text-decoration: none;
}

.skip-link:focus {
  top: 0;
}
</style>
```

#### 2.4.2 Page Titled (Level A)

Web pages have titles that describe topic or purpose.

**Good examples:**
- "Computer Science MSc - Courses - University of Sheffield"
- "Contact Us - University of Sheffield"
- "Research Output: Quantum Computing - University of Sheffield"

**Bad examples:**
- "Page 1"
- "Untitled"
- Same title on every page

#### 2.4.3 Focus Order (Level A)

If a Web page can be navigated sequentially and the navigation sequences affect meaning or operation, focusable components receive focus in an order that preserves meaning and operability.

#### 2.4.4 Link Purpose (In Context) (Level A)

The purpose of each link can be determined from the link text alone or from the link text together with its programmatically determined link context.

**Implementation:**
```html
<!-- Bad -->
<a href="/report.pdf">Click here</a>

<!-- Good -->
<a href="/report.pdf">Annual Research Report 2024 (PDF, 2.3MB)</a>

<!-- Good with context -->
<p>Our latest research on quantum computing is now available.</p>
<a href="/quantum-research">Learn more</a>
```

#### 2.4.5 Multiple Ways (Level AA)

More than one way is available to locate a Web page within a set of Web pages except where the Web Page is the result of, or a step in, a process.

**Examples of multiple ways:**
- Site search
- Site map
- Navigation menus
- Breadcrumbs
- Related links

#### 2.4.6 Headings and Labels (Level AA)

Headings and labels describe topic or purpose.

**Good headings:**
- Descriptive of content
- Unique within page
- In logical hierarchy
- Not used for styling

#### 2.4.7 Focus Visible (Level AA)

Any keyboard operable user interface has a mode of operation where the keyboard focus indicator is visible.

**Implementation:**
```css
/* Good focus indicator */
:focus {
  outline: 2px solid #005eb8;
  outline-offset: 2px;
}

/* Don't do this */
:focus {
  outline: none; /* Removes focus indicator */
}
```

### Guideline 2.5: Input Modalities

Make it easier for users to operate functionality through various inputs beyond keyboard.

#### 2.5.1 Pointer Gestures (Level A)

All functionality that uses multipoint or path-based gestures for operation can be operated with a single pointer without a path-based gesture, unless a multipoint or path-based gesture is essential.

#### 2.5.2 Pointer Cancellation (Level A)

For functionality that can be operated using a single pointer, at least one of the following is true:

**No Down-Event:** The down-event of the pointer is not used to execute any part of the function
**Abort or Undo:** Completion of the function is on the up-event, and a mechanism is available to abort the function before completion or to undo the function after completion
**Up Reversal:** The up-event reverses any outcome of the preceding down-event
**Essential:** Completing the function on the down-event is essential

#### 2.5.3 Label in Name (Level A)

For user interface components with labels that include text or images of text, the name contains the text that is presented visually.

**Implementation:**
```html
<!-- Visual label: "Search" -->
<!-- Good: aria-label matches or contains "Search" -->
<button aria-label="Search">
  <span class="icon-search"></span>
  Search
</button>

<!-- Bad: aria-label doesn't match visual label -->
<button aria-label="Find">
  <span class="icon-search"></span>
  Search
</button>
```

#### 2.5.4 Motion Actuation (Level A)

Functionality that can be operated by device motion or user motion can also be operated by user interface components and responding to the motion can be disabled to prevent accidental actuation.

---

## Principle 3: Understandable

Information and the operation of user interface must be understandable.

### Guideline 3.1: Readable

Make text content readable and understandable.

#### 3.1.1 Language of Page (Level A)

The default human language of each Web page can be programmatically determined.

**Implementation:**
```html
<html lang="en">
  <!-- English content -->
</html>

<html lang="es">
  <!-- Spanish content -->
</html>
```

#### 3.1.2 Language of Parts (Level AA)

The human language of each passage or phrase in the content can be programmatically determined except for proper names, technical terms, words of indeterminate language, and words or phrases that have become part of the vernacular of the immediately surrounding text.

**Implementation:**
```html
<p>The University motto is <span lang="la">Rerum cognoscere causas</span>.</p>
```

### Guideline 3.2: Predictable

Make Web pages appear and operate in predictable ways.

#### 3.2.1 On Focus (Level A)

When any user interface component receives focus, it does not initiate a change of context.

**Don't do:**
- Automatically submit form when field receives focus
- Open new window when element receives focus
- Change content dramatically when element receives focus

#### 3.2.2 On Input (Level A)

Changing the setting of any user interface component does not automatically cause a change of context unless the user has been advised of the behavior before using the component.

**Don't do:**
- Automatically submit form when dropdown selected (unless warned)
- Navigate to new page when radio button selected

**Do:**
- Provide submit button for forms
- Warn user if selection causes navigation

#### 3.2.3 Consistent Navigation (Level AA)

Navigational mechanisms that are repeated on multiple Web pages within a set of Web pages occur in the same relative order each time they are repeated, unless a change is initiated by the user.

#### 3.2.4 Consistent Identification (Level AA)

Components that have the same functionality within a set of Web pages are identified consistently.

**Example:**
- If a search icon is labeled "Search" on one page, use "Search" (not "Find") on all pages
- If a download link uses a specific icon, use the same icon consistently

### Guideline 3.3: Input Assistance

Help users avoid and correct mistakes.

#### 3.3.1 Error Identification (Level A)

If an input error is automatically detected, the item that is in error is identified and the error is described to the user in text.

**Implementation:**
```html
<label for="email">Email *</label>
<input type="email"
       id="email"
       aria-invalid="true"
       aria-describedby="email-error">
<span id="email-error" role="alert">
  Please enter a valid email address
</span>
```

#### 3.3.2 Labels or Instructions (Level A)

Labels or instructions are provided when content requires user input.

**Good examples:**
- Clear field labels
- Required field indicators
- Format instructions (e.g., "DD/MM/YYYY")
- Help text for complex fields

#### 3.3.3 Error Suggestion (Level AA)

If an input error is automatically detected and suggestions for correction are known, then the suggestions are provided to the user, unless it would jeopardize the security or purpose of the content.

**Implementation:**
```html
<span id="password-error" role="alert">
  Password must contain at least 8 characters, including one uppercase letter and one number
</span>
```

#### 3.3.4 Error Prevention (Legal, Financial, Data) (Level AA)

For Web pages that cause legal commitments or financial transactions for the user to occur, that modify or delete user-controllable data in data storage systems, or that submit user test responses, at least one of the following is true:

**Reversible:** Submissions are reversible
**Checked:** Data entered by the user is checked for input errors and the user is provided an opportunity to correct them
**Confirmed:** A mechanism is available for reviewing, confirming, and correcting information before finalizing the submission

---

## Principle 4: Robust

Content must be robust enough that it can be interpreted by a wide variety of user agents, including assistive technologies.

### Guideline 4.1: Compatible

Maximize compatibility with current and future user agents, including assistive technologies.

#### 4.1.1 Parsing (Level A)

In content implemented using markup languages, elements have complete start and end tags, elements are nested according to their specifications, elements do not contain duplicate attributes, and any IDs are unique.

**Note:** This criterion is obsolete in WCAG 2.2

#### 4.1.2 Name, Role, Value (Level A)

For all user interface components, the name and role can be programmatically determined; states, properties, and values that can be set by the user can be programmatically set; and notification of changes to these items is available to user agents, including assistive technologies.

**Implementation:**
```html
<!-- Native HTML provides name, role, value -->
<button type="button">Submit</button>

<!-- Custom widget needs ARIA -->
<div role="button"
     tabindex="0"
     aria-label="Close dialog"
     aria-pressed="false">
  X
</div>

<!-- Toggle button -->
<button type="button"
        aria-pressed="true"
        aria-label="Bold">
  <strong>B</strong>
</button>
```

#### 4.1.3 Status Messages (Level AA)

In content implemented using markup languages, status messages can be programmatically determined through role or properties such that they can be presented to the user by assistive technologies without receiving focus.

**Implementation:**
```html
<!-- Success message -->
<div role="status" aria-live="polite">
  Your changes have been saved
</div>

<!-- Error message -->
<div role="alert" aria-live="assertive">
  An error occurred while saving
</div>

<!-- Progress indicator -->
<div role="status" aria-live="polite" aria-atomic="true">
  Loading: 75% complete
</div>
```

---

## Quick Reference by Use Case

### Forms
- 1.3.1: Label/input associations
- 1.3.5: Autocomplete attributes
- 3.3.1: Error identification
- 3.3.2: Labels and instructions
- 3.3.3: Error suggestions
- 3.3.4: Error prevention (important forms)
- 4.1.2: Name, role, value

### Images
- 1.1.1: Alt text
- 1.4.5: Avoid images of text
- 1.4.11: Graphical object contrast (3:1)

### Navigation
- 2.4.1: Skip links
- 2.4.2: Page titles
- 2.4.3: Focus order
- 2.4.4: Link purpose
- 2.4.5: Multiple ways (AA)
- 2.4.7: Focus visible (AA)
- 3.2.3: Consistent navigation (AA)

### Color & Contrast
- 1.4.1: Don't use color alone
- 1.4.3: Text contrast 4.5:1 (AA)
- 1.4.11: UI component contrast 3:1 (AA)

### Multimedia
- 1.2.1: Audio/video alternatives
- 1.2.2: Captions (prerecorded)
- 1.2.4: Captions (live) (AA)
- 1.2.5: Audio description (AA)

### Structure
- 1.3.1: Semantic HTML
- 1.3.2: Meaningful sequence
- 2.4.6: Descriptive headings (AA)

### Keyboard
- 2.1.1: Keyboard access
- 2.1.2: No keyboard trap
- 2.4.7: Visible focus (AA)
