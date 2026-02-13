"""
Unit tests for Aegis Core PII scrubbing functionality
"""

import pytest
from aegis_core.server import scrub_pii


class TestPIIScrubbing:
    """Test cases for PII scrubbing functionality"""

    def test_scrub_person_name(self):
        """Test that person names are properly scrubbed"""
        text = "John Smith works here"
        result = scrub_pii(text)
        assert "<PERSON>" in result
        assert "John Smith" not in result

    def test_scrub_australian_tfn(self):
        """Test that Australian TFNs are properly scrubbed"""
        text = "TFN is 123456782"
        result = scrub_pii(text)
        assert "<AU_TFN>" in result
        assert "123456782" not in result

    def test_scrub_both_name_and_tfn(self):
        """Test that both names and TFNs are scrubbed together"""
        text = "Jane Doe's TFN is 876543210"
        result = scrub_pii(text)
        assert "<PERSON>" in result
        assert "<AU_TFN>" in result
        assert "Jane Doe" not in result
        assert "876543210" not in result

    def test_no_pii_returns_unchanged(self):
        """Test that text without PII is returned unchanged"""
        text = "This is a simple text without any PII"
        result = scrub_pii(text)
        assert result == text

    def test_multiple_persons(self):
        """Test scrubbing multiple person names"""
        text = "Meeting with Sarah Johnson and Michael Brown"
        result = scrub_pii(text)
        assert result.count("<PERSON>") == 2
        assert "Sarah Johnson" not in result
        assert "Michael Brown" not in result
