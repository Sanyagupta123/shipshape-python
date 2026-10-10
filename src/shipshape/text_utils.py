"""Utility functions for basic text normalization and email extraction."""

from __future__ import annotations

import re

_EMAIL_PATTERN = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")


def normalize_text(text: str) -> str:
    """Trim surrounding whitespace and collapse repeated whitespace.

    This treats tabs, newlines, and repeated spaces as a single separator.
    """
    return " ".join(text.split())


def count_words(text: str) -> int:
    """Count the whitespace-separated words in a string."""
    return len(text.split())


def extract_emails(text: str) -> list[str]:
    """Extract common email-shaped strings from text.

    The pattern intentionally matches simple email-like strings but does not
    attempt full RFC 5322 validation for every possible email address.
    """
    return _EMAIL_PATTERN.findall(text)
