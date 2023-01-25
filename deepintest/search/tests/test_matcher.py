"""
Testing module for the deepingtest.search.matcher module.
"""


import pytest
from ..matcher import Matcher


class TestMatcher:
    """The test class associated with the Matcher class."""

    def test_constructor_fails_when_term_is_wrong_type(self):
        """
        Tests if Matcher's constructor returns a `TypeError` when the
        search_term parameter is not a str.
        """
        tests = [1, ["a"], {"one": 1}]
        for elem in tests:
            with pytest.raises(TypeError):
                Matcher(search_term=elem)

    def test_constructor_fails_when_term_is_wrong_value(self):
        """
        Tests if Matcher's constructor returns a `ValueError` when the
        search_term parameter is an empty str or a str of spaces.
        """
        tests = ["", " ", "  ", "ab cd"]
        for elem in tests:
            with pytest.raises(ValueError):
                Matcher(search_term=elem)

    def test_match_fails_when_line_is_wrong_type(self):
        """
        Tests if Matcher.match returns a `TypeError` when the line
        parameter is not a str.
        """
        tests = [1, ["a"], {"one": 1}]
        matcher = Matcher("A")
        for elem in tests:
            with pytest.raises(TypeError):
                matcher.match(elem)

    def test_match_returns_the_proper_value(self):
        """
        Tests if Matcher.match returns a `TypeError` when the line
        parameter is not a str.
        """
        matcher = Matcher("ab")
        assert matcher.match("ab")
        assert matcher.match("ac ab a")
        assert not matcher.match("ac")
        assert not matcher.match("ac a b a")
