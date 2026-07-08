#!/usr/bin/env python3
"""
WCAG Color Contrast Checker

Validates color contrast ratios against WCAG 2.1 Level AA and AAA requirements.
Supports hex colors, RGB, and named colors.

Usage:
    python contrast_checker.py "#FFFFFF" "#000000"
    python contrast_checker.py "rgb(255,255,255)" "rgb(0,0,0)"
    python contrast_checker.py "#FFFFFF" "#000000" --level AAA
    python contrast_checker.py "#FFFFFF" "#000000" --large-text

Requirements:
    Standard library only - no external dependencies needed

WCAG Requirements:
    Level AA:
        - Normal text: 4.5:1 minimum
        - Large text (18pt+ or 14pt+ bold): 3:1 minimum
        - UI components: 3:1 minimum

    Level AAA:
        - Normal text: 7:1 minimum
        - Large text: 4.5:1 minimum
"""

import sys
import re
from typing import Tuple


class ColorContrastChecker:
    """Check color contrast ratios for WCAG compliance"""

    # Common named colors
    NAMED_COLORS = {
        'white': '#FFFFFF',
        'black': '#000000',
        'red': '#FF0000',
        'green': '#008000',
        'blue': '#0000FF',
        'yellow': '#FFFF00',
        'cyan': '#00FFFF',
        'magenta': '#FF00FF',
        'gray': '#808080',
        'grey': '#808080',
        'silver': '#C0C0C0',
        'maroon': '#800000',
        'olive': '#808000',
        'lime': '#00FF00',
        'aqua': '#00FFFF',
        'teal': '#008080',
        'navy': '#000080',
        'fuchsia': '#FF00FF',
        'purple': '#800080',
    }

    def __init__(self):
        pass

    def parse_color(self, color_str: str) -> Tuple[int, int, int]:
        """Parse color string to RGB tuple"""
        color_str = color_str.strip().lower()

        # Check for named color
        if color_str in self.NAMED_COLORS:
            color_str = self.NAMED_COLORS[color_str]

        # Parse hex color
        hex_match = re.match(r'#?([0-9a-f]{6})', color_str)
        if hex_match:
            hex_color = hex_match.group(1)
            return (
                int(hex_color[0:2], 16),
                int(hex_color[2:4], 16),
                int(hex_color[4:6], 16)
            )

        # Parse short hex color (#RGB -> #RRGGBB)
        short_hex_match = re.match(r'#?([0-9a-f])([0-9a-f])([0-9a-f])$', color_str)
        if short_hex_match:
            r, g, b = short_hex_match.groups()
            return (int(r + r, 16), int(g + g, 16), int(b + b, 16))

        # Parse rgb() format
        rgb_match = re.match(r'rgb\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)', color_str)
        if rgb_match:
            return tuple(map(int, rgb_match.groups()))

        raise ValueError(f"Could not parse color: {color_str}")

    def get_relative_luminance(self, rgb: Tuple[int, int, int]) -> float:
        """Calculate relative luminance for RGB color"""
        # Convert to sRGB
        r, g, b = [val / 255.0 for val in rgb]

        # Apply gamma correction
        def adjust(channel):
            if channel <= 0.03928:
                return channel / 12.92
            return ((channel + 0.055) / 1.055) ** 2.4

        r_lin = adjust(r)
        g_lin = adjust(g)
        b_lin = adjust(b)

        # Calculate luminance
        return 0.2126 * r_lin + 0.7152 * g_lin + 0.0722 * b_lin

    def get_contrast_ratio(self, color1: str, color2: str) -> float:
        """Calculate contrast ratio between two colors"""
        rgb1 = self.parse_color(color1)
        rgb2 = self.parse_color(color2)

        lum1 = self.get_relative_luminance(rgb1)
        lum2 = self.get_relative_luminance(rgb2)

        # Ensure lighter color is in numerator
        lighter = max(lum1, lum2)
        darker = min(lum1, lum2)

        return (lighter + 0.05) / (darker + 0.05)

    def check_wcag_compliance(self, foreground: str, background: str,
                             level: str = 'AA', large_text: bool = False) -> dict:
        """
        Check WCAG compliance for color combination

        Returns dict with:
            - ratio: contrast ratio
            - level: WCAG level checked
            - large_text: whether large text rules apply
            - passes: boolean indicating if contrast is sufficient
            - required: minimum ratio required
            - grade: descriptive grade (Fail, AA, AAA)
        """
        ratio = self.get_contrast_ratio(foreground, background)

        # Determine required ratio
        if level == 'AAA':
            required = 4.5 if large_text else 7.0
        else:  # AA
            required = 3.0 if large_text else 4.5

        passes = ratio >= required

        # Determine grade
        if ratio >= 7.0:
            grade = 'AAA' if not large_text else 'AAA+'
        elif ratio >= 4.5:
            grade = 'AAA' if large_text else 'AA'
        elif ratio >= 3.0:
            grade = 'AA' if large_text else 'Fail'
        else:
            grade = 'Fail'

        return {
            'ratio': ratio,
            'level': level,
            'large_text': large_text,
            'passes': passes,
            'required': required,
            'grade': grade,
            'foreground': foreground,
            'background': background
        }


def format_result(result: dict) -> str:
    """Format contrast check result as readable text"""
    lines = []
    lines.append("\n" + "=" * 60)
    lines.append("WCAG COLOR CONTRAST CHECK")
    lines.append("=" * 60)
    lines.append(f"\nForeground: {result['foreground']}")
    lines.append(f"Background: {result['background']}")
    lines.append(f"\nContrast Ratio: {result['ratio']:.2f}:1")
    lines.append(f"Required Ratio: {result['required']:.1f}:1 (Level {result['level']}, {'Large' if result['large_text'] else 'Normal'} text)")

    # Pass/fail status
    status_symbol = "✓" if result['passes'] else "✗"
    status_text = "PASS" if result['passes'] else "FAIL"
    lines.append(f"\nStatus: {status_symbol} {status_text}")
    lines.append(f"Grade: {result['grade']}")

    # Additional guidance
    lines.append("\n" + "-" * 60)
    lines.append("WCAG 2.1 Requirements:")
    lines.append("  Normal text (< 18pt or < 14pt bold):")
    lines.append(f"    Level AA:  4.5:1 {'✓' if result['ratio'] >= 4.5 else '✗'}")
    lines.append(f"    Level AAA: 7.0:1 {'✓' if result['ratio'] >= 7.0 else '✗'}")
    lines.append("  Large text (≥ 18pt or ≥ 14pt bold):")
    lines.append(f"    Level AA:  3.0:1 {'✓' if result['ratio'] >= 3.0 else '✗'}")
    lines.append(f"    Level AAA: 4.5:1 {'✓' if result['ratio'] >= 4.5 else '✗'}")

    if not result['passes']:
        lines.append("\n" + "-" * 60)
        lines.append("Suggestions:")
        if result['ratio'] < 3.0:
            lines.append("  • Contrast is very low - consider a completely different color")
        elif result['ratio'] < 4.5:
            if result['large_text']:
                lines.append("  • Acceptable for large text only (18pt+ or 14pt+ bold)")
            else:
                lines.append("  • Darken the foreground or lighten the background")
                lines.append("  • Or use only for large text (18pt+ or 14pt+ bold)")
        elif result['ratio'] < 7.0 and result['level'] == 'AAA':
            lines.append("  • Meets AA but not AAA - consider increasing contrast for AAA")

    lines.append("=" * 60 + "\n")

    return "\n".join(lines)


def suggest_adjustments(foreground: str, background: str, target_ratio: float = 4.5):
    """Suggest color adjustments to meet target ratio"""
    checker = ColorContrastChecker()
    fg_rgb = checker.parse_color(foreground)
    bg_rgb = checker.parse_color(background)

    print(f"\nSuggestions to achieve {target_ratio}:1 ratio:")
    print("-" * 60)

    # Try darkening foreground
    for adjustment in [20, 40, 60, 80, 100]:
        adjusted_fg = tuple(max(0, val - adjustment) for val in fg_rgb)
        adjusted_hex = '#{:02x}{:02x}{:02x}'.format(*adjusted_fg)
        ratio = checker.get_contrast_ratio(adjusted_hex, background)
        if ratio >= target_ratio:
            print(f"✓ Darken foreground to {adjusted_hex} → {ratio:.2f}:1")
            break

    # Try lightening background
    for adjustment in [20, 40, 60, 80, 100]:
        adjusted_bg = tuple(min(255, val + adjustment) for val in bg_rgb)
        adjusted_hex = '#{:02x}{:02x}{:02x}'.format(*adjusted_bg)
        ratio = checker.get_contrast_ratio(foreground, adjusted_hex)
        if ratio >= target_ratio:
            print(f"✓ Lighten background to {adjusted_hex} → {ratio:.2f}:1")
            break


def main():
    """Main entry point"""
    if len(sys.argv) < 3:
        print(__doc__)
        print("\nExamples:")
        print('  python contrast_checker.py "#000000" "#FFFFFF"')
        print('  python contrast_checker.py "rgb(0,0,0)" "#FFF"')
        print('  python contrast_checker.py "#767676" "white" --level AAA')
        print('  python contrast_checker.py "#999" "#FFF" --large-text')
        sys.exit(1)

    foreground = sys.argv[1]
    background = sys.argv[2]
    level = 'AA'
    large_text = False
    show_suggestions = False

    # Parse options
    if '--level' in sys.argv:
        idx = sys.argv.index('--level')
        if idx + 1 < len(sys.argv):
            level = sys.argv[idx + 1].upper()

    if '--large-text' in sys.argv:
        large_text = True

    if '--suggest' in sys.argv:
        show_suggestions = True

    try:
        checker = ColorContrastChecker()
        result = checker.check_wcag_compliance(foreground, background, level, large_text)
        print(format_result(result))

        if show_suggestions and not result['passes']:
            suggest_adjustments(foreground, background, result['required'])

        # Exit with error code if fails
        sys.exit(0 if result['passes'] else 1)

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == '__main__':
    main()
