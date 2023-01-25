"""
Testing module for the deepingtest.search.cleaner module.
"""


import pytest
from ..cleaner import Cleaner


class TestCleaner:
    """The test class associated with the Cleaner class."""

    def test_constructor_with_wrong_characters_parameter_fails(self):
        """
        Tests if constructor returns a `TypeError` when the provided parameter
        is not a list of characters or character range.
        """
        tests = ["a", 1, {"one": 1}, ("a", ("a", "b")), [1, ("a", "b")], [1, (1, "b")]]
        for elem in tests:
            with pytest.raises(TypeError):
                Cleaner(elem)

    def test_clean_line_returns_proper_result(self):
        """
        Tests if Cleaner.clean_line returns the appropriate str for a
        given input.
        """
        cleaner = Cleaner()
        tests = [
            ("""908^)-234 923this-++-23is./<.";][}"another-=&^5""", "this is another"),
            ("""the ^----;:[]}< <!!<**& lazy $$$~~~)))dog""", "the lazy dog"),
            ("""===--le-!!!**manège*&""$" enchanté   """, "le manège enchanté"),
        ]
        for line, result in tests:
            assert cleaner.clean_line(line) == result

    def test_clean_line_returns_proper_result_with_delimiter(self):
        """
        Tests if Cleaner.clean_line returns the appropriate str for a
        given input and delimiter.
        """
        cleaner = Cleaner(delimiter=":")
        tests = [
            (
                """::908^)-234 923this-+::+-23is./<.";][}":another-=&^5""",
                "this:is:another",
            ),
            (
                """the ^----;:[]}< <!!<**& little:lazy $$$~~~)))dog""",
                "the:little:lazy:dog",
            ),
            ("""===--le-!!!**manège:*&""$":enchanté   """, "le:manège:enchanté"),
        ]
        for line, result in tests:
            assert cleaner.clean_line(line) == result
