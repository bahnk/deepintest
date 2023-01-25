"""
Testing module for the deepingtest.search.characters module.
"""


import pytest
from ..characters import CharacterRange
from ..characters import CharacterSet


class TestCharacterRange:
    """The test class associated with the CharacterRange class."""

    def test_constructor_fails_with_wrong_parameter(self):
        """
        Tests if CharactersRange's constructor returns a `TypeError` when the
        provided parameter is not a tuple of two characters.
        """
        tests = ["a", 1, "aaa", ["a"], ["a", "z"], ("aa", "b"), (1, "b")]
        for elem in tests:
            with pytest.raises(TypeError):
                CharacterRange(elem)

    def test_get_characters_returns_the_proper_list(self):
        """
        Tests if CharactersRange.get_characters return the appropriate list
        of characters.
        """
        tests = [
            (("A", "C"), ["A", "B", "C"]),
            (("z", "w"), ["w", "x", "y", "z"]),
            (("a", "a"), ["a"]),
        ]
        for char_range, result in tests:
            crange = CharacterRange(character_range=char_range)
            assert crange.get_characters() == result


class TestCharacterSet:
    """The test class associated with the CharacterSet class."""

    def test_constructor_fails_with_wrong_parameter(self):
        """
        Tests if CharactersSet's constructor returns a `TypeError` when the
        provided parameter is not a list of characters or character ranges.
        """
        tests = ["a", 1, {"one": 1}, ("a", ("a", "b")), [1, ("a", "b")], [1, (1, "b")]]
        for elem in tests:
            with pytest.raises(TypeError):
                CharacterSet(elem)

    def test_get_characters_returns_the_proper_set(self):
        """
        Tests if CharactersSet.get_characters return the appropriate set
        of characters.
        """
        tests = [
            ([("A", "C"), "D"], {"A", "B", "C", "D"}),
            (["D", ("A", "C"), "A"], {"A", "B", "C", "D"}),
            (["D", ("A", "C"), "A"], {"A", "B", "C", "D"}),
            ([("À", "Â")], {"À", "Á", "Â"}),
        ]
        for characters, result in tests:
            charset = CharacterSet(characters=characters)
            assert charset.get_characters() == result

    def test_add_character_fails_with_wrong_parameter(self):
        """
        Tests if Characters.add_character returns a `TypeError` when the provided
        parameter is not a character.
        """
        charset = CharacterSet(characters=[("A", "C")])
        tests = [1, 0.5, 0x45, "aa", ["a", 5], ("ab", "cd"), {"one": 1}]
        for elem in tests:
            with pytest.raises(TypeError):
                charset.add_character(elem)

    def test_add_character_adds_the_character(self):
        """
        Tests if CharactersSet.add_character add the character to the set
        of supported characters.
        """
        charset = CharacterSet(characters=[("A", "C")])
        charset.add_character("D")
        assert charset.get_characters() == {"A", "B", "C", "D"}
