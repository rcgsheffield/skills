# ARIA Design Patterns Reference

Comprehensive reference for implementing accessible custom widgets using ARIA (Accessible Rich Internet Applications).

## Table of Contents

- [ARIA Fundamentals](#aria-fundamentals)
- [Common Patterns](#common-patterns)
  - [Accordion](#accordion)
  - [Alert & Alert Dialog](#alert--alert-dialog)
  - [Breadcrumb](#breadcrumb)
  - [Button](#button)
  - [Dialog (Modal)](#dialog-modal)
  - [Disclosure (Show/Hide)](#disclosure-showhide)
  - [Menu & Menu Button](#menu--menu-button)
  - [Tabs](#tabs)
  - [Tooltip](#tooltip)
  - [Combobox (Autocomplete)](#combobox-autocomplete)
  - [Tree View](#tree-view)

---

## ARIA Fundamentals

### The Five Rules of ARIA

1. **Don't use ARIA if you can use native HTML**
   - Use `<button>` not `<div role="button">`
   - Use `<nav>` not `<div role="navigation">`

2. **Don't change native semantics**
   - Bad: `<h1 role="button">Click me</h1>`
   - Good: `<button>Click me</button>`

3. **All interactive ARIA controls must be keyboard accessible**
   - If you add `role="button"`, you must handle Enter/Space keys

4. **Don't use `role="presentation"` or `aria-hidden="true"` on focusable elements**
   - This creates confusion between keyboard and screen reader

5. **All interactive elements must have an accessible name**
   - Via label, aria-label, or aria-labelledby

### ARIA Attributes Quick Reference

**Roles** - What something is
- `role="button"`, `role="dialog"`, `role="tab"`, etc.

**States** - Current condition (can change)
- `aria-expanded`, `aria-checked`, `aria-pressed`, `aria-selected`

**Properties** - Relationships and descriptions (usually static)
- `aria-label`, `aria-labelledby`, `aria-describedby`, `aria-controls`

**Live Regions** - Dynamic content announcements
- `aria-live`, `role="alert"`, `role="status"`

---

## Common Patterns

### Accordion

Vertically stacked set of interactive headings that each contain a title for a section of content.

**Structure:**
```html
<div class="accordion">
  <!-- Accordion Item 1 -->
  <h3>
    <button type="button"
            aria-expanded="true"
            aria-controls="panel1"
            id="accordion1-button">
      Section 1 Title
    </button>
  </h3>
  <div id="panel1"
       role="region"
       aria-labelledby="accordion1-button">
    <p>Section 1 content...</p>
  </div>

  <!-- Accordion Item 2 -->
  <h3>
    <button type="button"
            aria-expanded="false"
            aria-controls="panel2"
            id="accordion2-button">
      Section 2 Title
    </button>
  </h3>
  <div id="panel2"
       role="region"
       aria-labelledby="accordion2-button"
       hidden>
    <p>Section 2 content...</p>
  </div>
</div>
```

**Keyboard Interaction:**
- `Enter` or `Space`: Toggle panel
- `Tab`: Move focus to next focusable element
- (Optional) `Down Arrow`: Move to next accordion button
- (Optional) `Up Arrow`: Move to previous accordion button
- (Optional) `Home`: Move to first accordion button
- (Optional) `End`: Move to last accordion button

**JavaScript Requirements:**
```javascript
button.addEventListener('click', () => {
  const expanded = button.getAttribute('aria-expanded') === 'true';
  button.setAttribute('aria-expanded', !expanded);
  panel.hidden = expanded;
});
```

---

### Alert & Alert Dialog

#### Alert
Important message that requires user's attention but not necessarily interaction.

**Structure:**
```html
<!-- Polite alert -->
<div role="status" aria-live="polite">
  Your changes have been saved
</div>

<!-- Assertive alert -->
<div role="alert" aria-live="assertive">
  Error: Unable to save your changes
</div>

<!-- Alert with heading -->
<div role="alert">
  <h2>Error Occurred</h2>
  <p>Unable to connect to server. Please try again.</p>
</div>
```

**Usage:**
- `role="alert"` implies `aria-live="assertive"` and `aria-atomic="true"`
- Use `role="status"` for less urgent messages
- Content is announced immediately when it appears
- Don't move focus to alert unless it requires user action

#### Alert Dialog
Modal dialog that requires user interaction before dismissing.

**Structure:**
```html
<div role="alertdialog"
     aria-modal="true"
     aria-labelledby="alert-title"
     aria-describedby="alert-desc">
  <h2 id="alert-title">Confirm Delete</h2>
  <p id="alert-desc">
    Are you sure you want to delete this item? This action cannot be undone.
  </p>
  <button type="button" onclick="confirmDelete()">Delete</button>
  <button type="button" onclick="closeDialog()">Cancel</button>
</div>
```

**Keyboard Interaction:**
- `Tab`: Move focus between dialog controls
- `Escape`: Close dialog (cancel action)
- `Enter`: Activate focused button

**JavaScript Requirements:**
- Move focus into dialog when opened
- Trap focus within dialog
- Restore focus to trigger element when closed

---

### Breadcrumb

Navigation path showing user's location in site hierarchy.

**Structure:**
```html
<nav aria-label="Breadcrumb">
  <ol>
    <li>
      <a href="/">Home</a>
    </li>
    <li>
      <a href="/research">Research</a>
    </li>
    <li>
      <a href="/research/departments">Departments</a>
    </li>
    <li aria-current="page">
      Computer Science
    </li>
  </ol>
</nav>
```

**Key Attributes:**
- `aria-label="Breadcrumb"` on `<nav>` to distinguish from main navigation
- `aria-current="page"` on current page item
- Use `<ol>` for semantic list structure

---

### Button

Clickable element that triggers an action.

**Native HTML (Preferred):**
```html
<button type="button">Click me</button>
```

**Custom Button (when necessary):**
```html
<div role="button"
     tabindex="0"
     onclick="doAction()"
     onkeydown="handleKeyDown(event)">
  Custom Button
</div>
```

**JavaScript for Custom Button:**
```javascript
function handleKeyDown(event) {
  // Activate on Enter or Space
  if (event.key === 'Enter' || event.key === ' ') {
    event.preventDefault();
    doAction();
  }
}
```

#### Toggle Button

Button that can be toggled on/off.

**Structure:**
```html
<button type="button"
        aria-pressed="false"
        onclick="toggleMute()">
  <span class="label">Mute</span>
</button>
```

**JavaScript:**
```javascript
function toggleMute() {
  const pressed = button.getAttribute('aria-pressed') === 'true';
  button.setAttribute('aria-pressed', !pressed);
  // Update button appearance and perform action
}
```

---

### Dialog (Modal)

Window overlaid on primary content, blocking interaction with the rest of the page.

**Structure:**
```html
<div role="dialog"
     aria-modal="true"
     aria-labelledby="dialog-title"
     aria-describedby="dialog-desc">

  <h2 id="dialog-title">Dialog Title</h2>

  <div id="dialog-desc">
    <p>Dialog content goes here...</p>
  </div>

  <div class="dialog-actions">
    <button type="button" onclick="closeDialog()">Close</button>
    <button type="button" onclick="confirmAction()">Confirm</button>
  </div>
</div>

<!-- Background overlay -->
<div class="dialog-backdrop" aria-hidden="true"></div>
```

**Keyboard Interaction:**
- `Tab`: Move focus forward through dialog controls
- `Shift + Tab`: Move focus backward
- `Escape`: Close dialog
- Focus must be trapped within dialog

**JavaScript Requirements:**
```javascript
function openDialog() {
  // 1. Store currently focused element
  previouslyFocused = document.activeElement;

  // 2. Show dialog
  dialog.style.display = 'block';

  // 3. Move focus into dialog (first focusable element or dialog itself)
  dialog.querySelector('button').focus();

  // 4. Prevent background scroll
  document.body.style.overflow = 'hidden';

  // 5. Set up focus trap
  setupFocusTrap(dialog);
}

function closeDialog() {
  // 1. Hide dialog
  dialog.style.display = 'none';

  // 2. Restore scroll
  document.body.style.overflow = '';

  // 3. Return focus to trigger element
  previouslyFocused.focus();
}

function setupFocusTrap(container) {
  const focusableElements = container.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  const firstElement = focusableElements[0];
  const lastElement = focusableElements[focusableElements.length - 1];

  container.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === firstElement) {
        e.preventDefault();
        lastElement.focus();
      } else if (!e.shiftKey && document.activeElement === lastElement) {
        e.preventDefault();
        firstElement.focus();
      }
    } else if (e.key === 'Escape') {
      closeDialog();
    }
  });
}
```

**CSS Considerations:**
```css
/* Ensure modal is visually on top */
[role="dialog"] {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1000;
}

.dialog-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  z-index: 999;
}
```

---

### Disclosure (Show/Hide)

Button that controls visibility of a section of content.

**Structure:**
```html
<button type="button"
        aria-expanded="false"
        aria-controls="content1">
  Show More Details
</button>

<div id="content1" hidden>
  <p>Additional content that can be shown or hidden...</p>
</div>
```

**Keyboard Interaction:**
- `Enter` or `Space`: Toggle content visibility

**JavaScript:**
```javascript
button.addEventListener('click', () => {
  const expanded = button.getAttribute('aria-expanded') === 'true';
  button.setAttribute('aria-expanded', !expanded);
  content.hidden = expanded;
  button.textContent = expanded ? 'Show More Details' : 'Hide Details';
});
```

---

### Menu & Menu Button

Button that opens a menu of choices.

**Structure:**
```html
<button type="button"
        aria-haspopup="true"
        aria-expanded="false"
        aria-controls="menu1">
  Actions
  <span aria-hidden="true">▼</span>
</button>

<ul role="menu"
    id="menu1"
    hidden>
  <li role="none">
    <button type="button" role="menuitem">Edit</button>
  </li>
  <li role="none">
    <button type="button" role="menuitem">Delete</button>
  </li>
  <li role="none">
    <button type="button" role="menuitem">Share</button>
  </li>
</ul>
```

**Keyboard Interaction (Menu Button):**
- `Enter` or `Space`: Open menu, focus first item
- `Down Arrow`: Open menu, focus first item
- `Up Arrow`: Open menu, focus last item

**Keyboard Interaction (Menu):**
- `Enter` or `Space`: Activate menu item, close menu
- `Down Arrow`: Focus next menu item (wrap to first)
- `Up Arrow`: Focus previous menu item (wrap to last)
- `Home`: Focus first menu item
- `End`: Focus last menu item
- `Escape`: Close menu, return focus to button
- `Tab`: Close menu, move to next focusable element

**JavaScript Requirements:**
```javascript
// Open menu
function openMenu() {
  menu.hidden = false;
  button.setAttribute('aria-expanded', 'true');
  menu.querySelector('[role="menuitem"]').focus();
}

// Close menu
function closeMenu() {
  menu.hidden = true;
  button.setAttribute('aria-expanded', 'false');
  button.focus();
}

// Arrow key navigation
menuItems.forEach((item, index) => {
  item.addEventListener('keydown', (e) => {
    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault();
        menuItems[(index + 1) % menuItems.length].focus();
        break;
      case 'ArrowUp':
        e.preventDefault();
        menuItems[(index - 1 + menuItems.length) % menuItems.length].focus();
        break;
      case 'Home':
        e.preventDefault();
        menuItems[0].focus();
        break;
      case 'End':
        e.preventDefault();
        menuItems[menuItems.length - 1].focus();
        break;
      case 'Escape':
        closeMenu();
        break;
    }
  });
});
```

---

### Tabs

Set of layered sections of content (tab panels) with controls (tabs) for displaying one panel at a time.

**Structure:**
```html
<div class="tabs">
  <div role="tablist" aria-label="Course Information">
    <button role="tab"
            aria-selected="true"
            aria-controls="panel-overview"
            id="tab-overview"
            tabindex="0">
      Overview
    </button>
    <button role="tab"
            aria-selected="false"
            aria-controls="panel-modules"
            id="tab-modules"
            tabindex="-1">
      Modules
    </button>
    <button role="tab"
            aria-selected="false"
            aria-controls="panel-fees"
            id="tab-fees"
            tabindex="-1">
      Fees
    </button>
  </div>

  <div role="tabpanel"
       id="panel-overview"
       aria-labelledby="tab-overview"
       tabindex="0">
    <h3>Course Overview</h3>
    <p>Overview content...</p>
  </div>

  <div role="tabpanel"
       id="panel-modules"
       aria-labelledby="tab-modules"
       tabindex="0"
       hidden>
    <h3>Course Modules</h3>
    <p>Modules content...</p>
  </div>

  <div role="tabpanel"
       id="panel-fees"
       aria-labelledby="tab-fees"
       tabindex="0"
       hidden>
    <h3>Fees & Funding</h3>
    <p>Fees content...</p>
  </div>
</div>
```

**Keyboard Interaction:**
- `Tab`: When focus moves into tab list, places focus on active tab
- `Left Arrow`: Focus previous tab, activate (automatic activation)
- `Right Arrow`: Focus next tab, activate (automatic activation)
- `Home`: Focus first tab, activate
- `End`: Focus last tab, activate
- `Delete` (optional): If deletion is supported

**Alternative: Manual Activation**
- Arrow keys only move focus
- `Enter` or `Space` activate focused tab

**JavaScript Requirements:**
```javascript
function selectTab(newTab) {
  // Deselect all tabs
  tabs.forEach(tab => {
    tab.setAttribute('aria-selected', 'false');
    tab.setAttribute('tabindex', '-1');
  });

  // Select new tab
  newTab.setAttribute('aria-selected', 'true');
  newTab.setAttribute('tabindex', '0');
  newTab.focus();

  // Hide all panels
  panels.forEach(panel => {
    panel.hidden = true;
  });

  // Show associated panel
  const panelId = newTab.getAttribute('aria-controls');
  document.getElementById(panelId).hidden = false;
}

// Arrow key navigation
tabs.forEach((tab, index) => {
  tab.addEventListener('keydown', (e) => {
    let newIndex;

    switch (e.key) {
      case 'ArrowLeft':
        newIndex = (index - 1 + tabs.length) % tabs.length;
        selectTab(tabs[newIndex]);
        break;
      case 'ArrowRight':
        newIndex = (index + 1) % tabs.length;
        selectTab(tabs[newIndex]);
        break;
      case 'Home':
        selectTab(tabs[0]);
        break;
      case 'End':
        selectTab(tabs[tabs.length - 1]);
        break;
    }
  });
});
```

---

### Tooltip

Popup that displays information related to an element when it receives keyboard focus or the mouse hovers over it.

**Structure:**
```html
<button type="button"
        aria-describedby="tooltip1">
  Help
  <span role="tooltip"
        id="tooltip1"
        hidden>
    Click for more information about this feature
  </span>
</button>
```

**CSS:**
```css
[role="tooltip"] {
  position: absolute;
  z-index: 1000;
  background: #000;
  color: #fff;
  padding: 4px 8px;
  border-radius: 4px;
}

/* Show on hover and focus */
button:hover [role="tooltip"],
button:focus [role="tooltip"] {
  display: block;
}
```

**JavaScript:**
```javascript
button.addEventListener('mouseenter', () => {
  tooltip.hidden = false;
});

button.addEventListener('mouseleave', () => {
  tooltip.hidden = true;
});

button.addEventListener('focus', () => {
  tooltip.hidden = false;
});

button.addEventListener('blur', () => {
  tooltip.hidden = true;
});

// Escape to dismiss
button.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    tooltip.hidden = true;
  }
});
```

**Important Notes:**
- Tooltips should be brief (under 150 characters)
- Don't put interactive content in tooltips
- Tooltip must be dismissible and hoverable (WCAG 1.4.13)
- Consider using `title` attribute for simple cases

---

### Combobox (Autocomplete)

Input field combined with a listbox that allows users to select from suggestions.

**Structure:**
```html
<label for="country">Country</label>
<div class="combobox">
  <input type="text"
         id="country"
         role="combobox"
         aria-expanded="false"
         aria-controls="country-listbox"
         aria-autocomplete="list"
         aria-activedescendant="">

  <ul id="country-listbox"
      role="listbox"
      hidden>
    <li role="option" id="option-1">United Kingdom</li>
    <li role="option" id="option-2">United States</li>
    <li role="option" id="option-3">Canada</li>
  </ul>
</div>
```

**Keyboard Interaction:**
- `Down Arrow`: Open listbox if closed; move to next option
- `Up Arrow`: Move to previous option
- `Enter`: Accept current option, close listbox
- `Escape`: Close listbox
- `Home`: Move to first option
- `End`: Move to last option
- Typing: Filter options

**JavaScript Requirements:**
```javascript
input.addEventListener('input', () => {
  const query = input.value.toLowerCase();
  const matches = options.filter(opt =>
    opt.textContent.toLowerCase().includes(query)
  );

  updateListbox(matches);

  if (matches.length > 0) {
    input.setAttribute('aria-expanded', 'true');
    listbox.hidden = false;
  } else {
    input.setAttribute('aria-expanded', 'false');
    listbox.hidden = true;
  }
});

input.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowDown') {
    e.preventDefault();
    if (listbox.hidden) {
      openListbox();
    } else {
      focusNextOption();
    }
  } else if (e.key === 'Escape') {
    closeListbox();
  }
});

function focusOption(option) {
  // Update aria-activedescendant
  input.setAttribute('aria-activedescendant', option.id);

  // Update visual focus
  options.forEach(opt => opt.classList.remove('focused'));
  option.classList.add('focused');

  // Scroll into view
  option.scrollIntoView({ block: 'nearest' });
}
```

---

### Tree View

Hierarchical list with expandable/collapsible nodes.

**Structure:**
```html
<ul role="tree" aria-label="File System">
  <li role="treeitem"
      aria-expanded="true"
      aria-level="1"
      aria-setsize="2"
      aria-posinset="1"
      tabindex="0">
    Documents
    <ul role="group">
      <li role="treeitem"
          aria-level="2"
          aria-setsize="2"
          aria-posinset="1"
          tabindex="-1">
        Report.pdf
      </li>
      <li role="treeitem"
          aria-level="2"
          aria-setsize="2"
          aria-posinset="2"
          tabindex="-1">
        Notes.txt
      </li>
    </ul>
  </li>
  <li role="treeitem"
      aria-expanded="false"
      aria-level="1"
      aria-setsize="2"
      aria-posinset="2"
      tabindex="-1">
    Images
  </li>
</ul>
```

**Keyboard Interaction:**
- `Down Arrow`: Move to next visible node
- `Up Arrow`: Move to previous visible node
- `Right Arrow`: Expand node if collapsed; move to first child if expanded
- `Left Arrow`: Collapse node if expanded; move to parent if collapsed
- `Home`: Move to first node
- `End`: Move to last visible node
- `Enter`: Activate node (open file, navigate, etc.)
- `*` (asterisk): Expand all siblings at same level

**JavaScript Requirements:**
- Manage `aria-expanded` state
- Update `tabindex` for roving tabindex pattern
- Handle arrow key navigation
- Ensure only one treeitem has `tabindex="0"`

---

## ARIA Live Regions

For announcing dynamic content changes to screen readers.

### aria-live

**Values:**
- `off` (default): No announcements
- `polite`: Announce when user is idle
- `assertive`: Interrupt user to announce immediately

**Usage:**
```html
<!-- Polite announcement -->
<div aria-live="polite" aria-atomic="true">
  3 items added to cart
</div>

<!-- Assertive announcement -->
<div aria-live="assertive" role="alert">
  Error: Payment failed
</div>
```

### aria-atomic

Determines whether entire region is announced or just changes.

- `true`: Announce entire region
- `false` (default): Announce only changes

### aria-relevant

Determines what changes should be announced.

- `additions`: Announce when nodes are added
- `removals`: Announce when nodes are removed
- `text`: Announce text changes
- `all`: Announce all changes

**Usage:**
```html
<div aria-live="polite"
     aria-atomic="false"
     aria-relevant="additions text">
  <!-- Dynamic content -->
</div>
```

### Common Live Region Roles

**role="status"**
- Advisory information
- Not important enough for alert
- Implicitly `aria-live="polite"`

```html
<div role="status">Loading...</div>
```

**role="alert"**
- Important, time-sensitive message
- Implicitly `aria-live="assertive"` and `aria-atomic="true"`

```html
<div role="alert">Form submission failed</div>
```

**role="log"**
- Sequential information like chat messages or logs
- New content added to end

```html
<div role="log" aria-live="polite">
  <p>User joined the chat</p>
  <p>New message received</p>
</div>
```

**role="timer"**
- Numerical counter indicating elapsed or remaining time

```html
<div role="timer" aria-live="off" aria-atomic="true">
  5:00 remaining
</div>
```

---

## Testing ARIA Implementations

### Screen Reader Testing

**Windows:**
- NVDA (free): Download from nvaccess.org
- JAWS (commercial): Most widely used in enterprise

**Mac:**
- VoiceOver (built-in): Cmd+F5 to toggle

**Mobile:**
- iOS VoiceOver: Settings > Accessibility > VoiceOver
- Android TalkBack: Settings > Accessibility > TalkBack

### Testing Checklist

- [ ] All interactive elements keyboard accessible
- [ ] Focus order logical
- [ ] All states announced correctly
- [ ] Dynamic content changes announced
- [ ] Relationships between elements clear
- [ ] All controls have accessible names
- [ ] ARIA doesn't override native semantics
- [ ] Works with screen reader in browse and focus modes

### Common Issues

**Issue:** Screen reader not announcing state changes
**Fix:** Ensure `aria-live` region exists in DOM before content changes

**Issue:** Too many announcements
**Fix:** Use `aria-atomic="false"` or debounce updates

**Issue:** Focus lost when content updates
**Fix:** Manage focus explicitly, use `aria-activedescendant` pattern

**Issue:** Keyboard trap
**Fix:** Ensure all modal content allows Escape key to exit

---

## Resources

**WAI-ARIA Authoring Practices:** https://www.w3.org/WAI/ARIA/apg/
**MDN ARIA Documentation:** https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA
**Inclusive Components:** https://inclusive-components.design/
**A11y Project Patterns:** https://www.a11yproject.com/patterns/
