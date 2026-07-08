#!/usr/bin/env python3
"""
Accessibility Audit Script for University of Sheffield Web Projects

This script performs automated accessibility checks on HTML files or directories.
It validates against WCAG 2.1 Level AA requirements.

Usage:
    python accessibility_audit.py <path_to_html_file_or_directory>
    python accessibility_audit.py <path> --format json
    python accessibility_audit.py <path> --wcag-level AAA

Requirements:
    pip install beautifulsoup4 lxml
"""

import sys
import os
import re
import json
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass, asdict

try:
    from bs4 import BeautifulSoup, Tag
except ImportError:
    print("Error: BeautifulSoup4 is required. Install with: pip install beautifulsoup4 lxml")
    sys.exit(1)


@dataclass
class AccessibilityIssue:
    """Represents a single accessibility issue"""
    severity: str  # 'error', 'warning', 'info'
    wcag_criterion: str
    message: str
    element: str
    line_number: int = 0
    suggestion: str = ""


class AccessibilityAuditor:
    """Performs accessibility audits on HTML content"""

    def __init__(self, wcag_level='AA'):
        self.wcag_level = wcag_level
        self.issues: List[AccessibilityIssue] = []

    def audit_html(self, html_content: str, filename: str = "") -> List[AccessibilityIssue]:
        """Main audit function"""
        self.issues = []
        soup = BeautifulSoup(html_content, 'lxml')

        # Run all checks
        self._check_images(soup)
        self._check_headings(soup)
        self._check_links(soup)
        self._check_forms(soup)
        self._check_page_structure(soup)
        self._check_semantic_html(soup)
        self._check_tables(soup)
        self._check_buttons(soup)
        self._check_language(soup)
        self._check_aria_usage(soup)

        return self.issues

    def _add_issue(self, severity: str, wcag: str, message: str,
                   element: Tag = None, suggestion: str = ""):
        """Helper to add an issue to the list"""
        element_str = str(element)[:100] if element else ""
        self.issues.append(AccessibilityIssue(
            severity=severity,
            wcag_criterion=wcag,
            message=message,
            element=element_str,
            suggestion=suggestion
        ))

    def _check_images(self, soup: BeautifulSoup):
        """Check image alt text - WCAG 1.1.1"""
        images = soup.find_all('img')

        for img in images:
            # Check for missing alt attribute
            if not img.has_attr('alt'):
                self._add_issue(
                    'error',
                    '1.1.1',
                    'Image missing alt attribute',
                    img,
                    'Add alt="" for decorative images or descriptive alt text for meaningful images'
                )

            # Check for suspicious alt text
            elif img.get('alt', '').strip():
                alt_text = img.get('alt', '').lower()
                suspicious_patterns = ['image of', 'picture of', 'graphic of', 'photo of']
                if any(pattern in alt_text for pattern in suspicious_patterns):
                    self._add_issue(
                        'warning',
                        '1.1.1',
                        f'Alt text may be overly descriptive: "{img.get("alt")}"',
                        img,
                        'Describe content/function, not that it\'s an image'
                    )

    def _check_headings(self, soup: BeautifulSoup):
        """Check heading hierarchy - WCAG 1.3.1, 2.4.6"""
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

        if not headings:
            self._add_issue(
                'warning',
                '2.4.6',
                'No headings found - consider adding headings for structure',
                suggestion='Use h1-h6 elements to provide page structure'
            )
            return

        # Check for h1
        h1_count = len(soup.find_all('h1'))
        if h1_count == 0:
            self._add_issue(
                'error',
                '2.4.6',
                'No h1 heading found',
                suggestion='Every page should have exactly one h1 element'
            )
        elif h1_count > 1:
            self._add_issue(
                'warning',
                '2.4.6',
                f'Multiple h1 headings found ({h1_count})',
                suggestion='Use only one h1 per page'
            )

        # Check heading hierarchy
        prev_level = 0
        for heading in headings:
            current_level = int(heading.name[1])

            if prev_level > 0 and current_level - prev_level > 1:
                self._add_issue(
                    'error',
                    '1.3.1',
                    f'Heading level skipped: {heading.name} follows h{prev_level}',
                    heading,
                    'Never skip heading levels (e.g., h1 → h3)'
                )

            # Check for empty headings
            if not heading.get_text(strip=True):
                self._add_issue(
                    'error',
                    '2.4.6',
                    f'Empty heading: {heading.name}',
                    heading,
                    'All headings must contain text content'
                )

            prev_level = current_level

    def _check_links(self, soup: BeautifulSoup):
        """Check link accessibility - WCAG 2.4.4"""
        links = soup.find_all('a')

        for link in links:
            link_text = link.get_text(strip=True)

            # Check for empty links
            if not link_text and not link.find('img'):
                self._add_issue(
                    'error',
                    '2.4.4',
                    'Empty link with no text or image',
                    link,
                    'Add descriptive link text or alt text on linked image'
                )

            # Check for generic link text
            generic_text = ['click here', 'read more', 'more', 'link', 'here']
            if link_text.lower() in generic_text:
                self._add_issue(
                    'warning',
                    '2.4.4',
                    f'Generic link text: "{link_text}"',
                    link,
                    'Use descriptive link text that makes sense out of context'
                )

            # Check for href
            if not link.has_attr('href') or not link.get('href').strip():
                self._add_issue(
                    'error',
                    '2.4.4',
                    'Link missing href attribute',
                    link,
                    'All links must have a valid href attribute'
                )

    def _check_forms(self, soup: BeautifulSoup):
        """Check form accessibility - WCAG 1.3.1, 3.3.2"""
        # Check inputs have labels
        inputs = soup.find_all(['input', 'select', 'textarea'])

        for input_elem in inputs:
            input_type = input_elem.get('type', 'text')

            # Skip hidden and submit/button types
            if input_type in ['hidden', 'submit', 'button', 'reset']:
                continue

            input_id = input_elem.get('id')
            aria_label = input_elem.get('aria-label')
            aria_labelledby = input_elem.get('aria-labelledby')

            # Check for label
            has_label = False
            if input_id:
                label = soup.find('label', {'for': input_id})
                if label:
                    has_label = True

            if not has_label and not aria_label and not aria_labelledby:
                self._add_issue(
                    'error',
                    '3.3.2',
                    f'Form input missing label: {input_elem.get("name", "unnamed")}',
                    input_elem,
                    'Associate a <label> element or add aria-label attribute'
                )

        # Check fieldsets have legends
        fieldsets = soup.find_all('fieldset')
        for fieldset in fieldsets:
            if not fieldset.find('legend'):
                self._add_issue(
                    'warning',
                    '1.3.1',
                    'Fieldset missing legend',
                    fieldset,
                    'Add <legend> to describe the group of form fields'
                )

    def _check_page_structure(self, soup: BeautifulSoup):
        """Check page structure - WCAG 1.3.1"""
        # Check for main landmark
        if not soup.find('main') and not soup.find(attrs={'role': 'main'}):
            self._add_issue(
                'warning',
                '1.3.1',
                'No main landmark found',
                suggestion='Add <main> element to identify main content'
            )

        # Check for navigation
        nav_elements = soup.find_all('nav') + soup.find_all(attrs={'role': 'navigation'})
        if len(nav_elements) > 1:
            # Check if navs have labels
            for nav in nav_elements:
                if not nav.get('aria-label') and not nav.get('aria-labelledby'):
                    self._add_issue(
                        'warning',
                        '1.3.1',
                        'Multiple navigation regions - consider adding aria-label',
                        nav,
                        'When multiple navs exist, label each: <nav aria-label="Main navigation">'
                    )

    def _check_semantic_html(self, soup: BeautifulSoup):
        """Check for semantic HTML usage"""
        # Check for excessive div/span usage
        divs = soup.find_all('div')

        for div in divs:
            # Check if div is used as button
            if div.get('onclick') or div.get('role') == 'button':
                self._add_issue(
                    'error',
                    '4.1.2',
                    'Div used as button',
                    div,
                    'Use <button> element instead of div with onclick'
                )

    def _check_tables(self, soup: BeautifulSoup):
        """Check table accessibility - WCAG 1.3.1"""
        tables = soup.find_all('table')

        for table in tables:
            # Check for caption
            if not table.find('caption'):
                self._add_issue(
                    'warning',
                    '1.3.1',
                    'Table missing caption',
                    table,
                    'Add <caption> to describe table purpose'
                )

            # Check for th elements
            if not table.find('th'):
                self._add_issue(
                    'warning',
                    '1.3.1',
                    'Table has no header cells (th)',
                    table,
                    'Use <th> elements for table headers'
                )

            # Check th elements have scope
            headers = table.find_all('th')
            for th in headers:
                if not th.get('scope'):
                    self._add_issue(
                        'warning',
                        '1.3.1',
                        'Table header missing scope attribute',
                        th,
                        'Add scope="col" or scope="row" to <th> elements'
                    )

    def _check_buttons(self, soup: BeautifulSoup):
        """Check button accessibility"""
        buttons = soup.find_all('button')

        for button in buttons:
            if not button.get_text(strip=True) and not button.find('img'):
                self._add_issue(
                    'error',
                    '4.1.2',
                    'Button has no text content',
                    button,
                    'Add text content or aria-label to button'
                )

    def _check_language(self, soup: BeautifulSoup):
        """Check language attributes - WCAG 3.1.1"""
        html_tag = soup.find('html')

        if html_tag and not html_tag.get('lang'):
            self._add_issue(
                'error',
                '3.1.1',
                'HTML element missing lang attribute',
                html_tag,
                'Add lang="en" to <html> element'
            )

    def _check_aria_usage(self, soup: BeautifulSoup):
        """Check ARIA usage patterns"""
        # Find elements with ARIA roles
        aria_elements = soup.find_all(attrs={'role': True})

        for elem in aria_elements:
            role = elem.get('role')

            # Check if native HTML should be used instead
            discouraged_roles = {
                'button': '<button>',
                'link': '<a href="">',
                'checkbox': '<input type="checkbox">',
                'radio': '<input type="radio">',
                'textbox': '<input type="text">',
            }

            if role in discouraged_roles:
                self._add_issue(
                    'warning',
                    '4.1.2',
                    f'ARIA role="{role}" used - native HTML preferred',
                    elem,
                    f'Use {discouraged_roles[role]} instead of ARIA role'
                )


def format_issues_text(issues: List[AccessibilityIssue], filename: str = "") -> str:
    """Format issues as human-readable text"""
    if not issues:
        return f"✓ No accessibility issues found{' in ' + filename if filename else ''}!"

    output = []
    output.append(f"\nAccessibility Audit Results{' for ' + filename if filename else ''}")
    output.append("=" * 60)

    # Group by severity
    errors = [i for i in issues if i.severity == 'error']
    warnings = [i for i in issues if i.severity == 'warning']
    info = [i for i in issues if i.severity == 'info']

    output.append(f"\nSummary: {len(errors)} errors, {len(warnings)} warnings, {len(info)} info")

    for severity, items in [('ERRORS', errors), ('WARNINGS', warnings), ('INFO', info)]:
        if items:
            output.append(f"\n{severity}:")
            output.append("-" * 60)
            for issue in items:
                output.append(f"\nWCAG {issue.wcag_criterion}: {issue.message}")
                if issue.element:
                    output.append(f"  Element: {issue.element}")
                if issue.suggestion:
                    output.append(f"  → {issue.suggestion}")

    return "\n".join(output)


def format_issues_json(issues: List[AccessibilityIssue]) -> str:
    """Format issues as JSON"""
    return json.dumps([asdict(issue) for issue in issues], indent=2)


def audit_file(filepath: Path, wcag_level: str = 'AA', output_format: str = 'text'):
    """Audit a single HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()

        auditor = AccessibilityAuditor(wcag_level)
        issues = auditor.audit_html(html_content, filepath.name)

        if output_format == 'json':
            print(format_issues_json(issues))
        else:
            print(format_issues_text(issues, filepath.name))

        return len([i for i in issues if i.severity == 'error'])

    except Exception as e:
        print(f"Error auditing {filepath}: {e}", file=sys.stderr)
        return 1


def audit_directory(dirpath: Path, wcag_level: str = 'AA', output_format: str = 'text'):
    """Audit all HTML files in a directory"""
    html_files = list(dirpath.rglob('*.html'))

    if not html_files:
        print(f"No HTML files found in {dirpath}")
        return 0

    print(f"Found {len(html_files)} HTML file(s) to audit\n")

    total_errors = 0
    for filepath in html_files:
        errors = audit_file(filepath, wcag_level, output_format)
        total_errors += errors
        if output_format == 'text':
            print("\n" + "=" * 60 + "\n")

    print(f"\nAudit complete: {len(html_files)} files checked")
    if total_errors > 0:
        print(f"⚠ Total errors found: {total_errors}")
        return 1
    else:
        print("✓ No critical errors found")
        return 0


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    path = Path(sys.argv[1])
    wcag_level = 'AA'
    output_format = 'text'

    # Parse options
    if '--wcag-level' in sys.argv:
        idx = sys.argv.index('--wcag-level')
        if idx + 1 < len(sys.argv):
            wcag_level = sys.argv[idx + 1]

    if '--format' in sys.argv:
        idx = sys.argv.index('--format')
        if idx + 1 < len(sys.argv):
            output_format = sys.argv[idx + 1]

    if not path.exists():
        print(f"Error: Path not found: {path}", file=sys.stderr)
        sys.exit(1)

    if path.is_file():
        exit_code = audit_file(path, wcag_level, output_format)
    else:
        exit_code = audit_directory(path, wcag_level, output_format)

    sys.exit(exit_code)


if __name__ == '__main__':
    main()
