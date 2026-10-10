"""Tests for the ShipShape text utility helpers."""

from shipshape import count_words, extract_emails, normalize_text


def test_normalize_text_collapses_repeated_whitespace() -> None:
    assert normalize_text("  hello   world  ") == "hello world"


def test_normalize_text_handles_tabs_and_newlines() -> None:
    assert normalize_text("\thello\n\tworld\n") == "hello world"


def test_normalize_text_handles_empty_strings() -> None:
    assert normalize_text("") == ""
    assert normalize_text("   ") == ""


def test_count_words_counts_whitespace_separated_tokens() -> None:
    assert count_words("Python makes useful tools") == 4


def test_count_words_handles_newlines_and_repeated_whitespace() -> None:
    assert count_words("one\n  two\tthree   four") == 4


def test_count_words_handles_empty_and_whitespace_only_text() -> None:
    assert count_words("") == 0
    assert count_words("   ") == 0


def test_extract_emails_returns_single_email() -> None:
    assert extract_emails("Contact a@example.com") == ["a@example.com"]


def test_extract_emails_returns_multiple_emails() -> None:
    result = extract_emails("Contact a@example.com or b@example.org")
    assert result == ["a@example.com", "b@example.org"]


def test_extract_emails_returns_empty_list_without_matches() -> None:
    assert extract_emails("No contact details here") == []


def test_extract_emails_handles_empty_input() -> None:
    assert extract_emails("") == []


def test_extract_emails_handles_punctuation_and_repeated_shapes() -> None:
    result = extract_emails("(a@example.com), <b@example.org>; a@example.com")
    assert result == ["a@example.com", "b@example.org", "a@example.com"]


def test_extract_emails_ignores_malformed_examples() -> None:
    assert extract_emails("bad@ localhost invalid@@example.com") == []
