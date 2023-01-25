"""
Module for characters manipulation.
"""

from typing import List, Set, Tuple

from deepintest._utils import _is_character
from deepintest._typing import Chars


class CharacterRange:
    """
    Convenience class used to return a character range in the unicode table.
    """

    _character_range: Tuple[str]
    _characters: List[str]

    def __init__(self, character_range: Tuple[str]) -> None:
        """\
        Constructor of the `CharacterRange` class.

        The constructor returns a `TypeError` if the `character_range` parameter is
        is not valid (should be a `tuple` of characters (`str` of size 1)).

        Parameters
        ----------
        character_range
            A `tuple` of character (`str` of size 1) representing the range in
            the encoding table.
            For example, ("A", "Z") or ("z", "a") are valid.
        """
        if self._is_valid_range(character_range):
            self._character_range = character_range
        else:
            raise TypeError(
                "The character_range parameter is not valid. "
                "The character_range parameter should be a tuple of two characters. "
                'For example, ("A", "Z"), ("z", "a") or ("é", "ç") '
                "are valid character ranges. "
            )
        self._characters = self._create_character_list(self._character_range)

    @property
    def characters(self) -> List[str]:
        """Returns the characters list."""
        return self._characters

    def _is_valid_range(self, character_range) -> bool:
        """Returns `True` if the provided character range is valid."""
        if not isinstance(character_range, tuple):
            return False
        if len(character_range) != 2:
            return False
        if set(map(type, character_range)) != {str}:
            return False
        if len(character_range[0]) != 1 or len(character_range[1]) != 1:
            return False
        return True

    def _create_character_list(self, character_range) -> List[int]:
        """Creates the characters list."""
        codes = sorted(list(map(ord, character_range)))
        code_range = list(range(codes[0], codes[1] + 1))
        return list(map(chr, code_range))

    def get_characters(self) -> List[int]:
        """Returns the characters list of the range."""
        return self._characters


class CharacterSet:
    """
    Convenience class used to represent a set of unicode characters.
    """

    _encoding: str
    _characters: Set[str]

    def __init__(self, characters: Chars) -> None:
        """\
        Constructor of the `CharacterSet` class.

        The constructor returns a `TypeError` if the `characters` parameter is
        is not valid.
        The `characters` parameter should be a `list` of characters
        (`str` of size 1) and/or `tuple` of characters.
        For example, `["A", ("B", "E"), "g", ("z", "v")]` is valid.

        Parameters
        ----------
        characters
            A `list` of characters (`str` of size 1) and/or `tuple` of characters.
            For example, `["A", ("B", "E"), "g", ("z", "v")]` is valid.
        """
        try:
            self._characters = self._create_character_set(characters)
        except TypeError as type_err:
            raise type_err

    def __contains__(self, character):
        return character in self._characters

    @property
    def characters(self) -> List[str]:
        """Returns the characters list."""
        return self._characters

    def _create_character_set(self, characters: Chars) -> Set[int]:
        """Returns the set of the supported characters."""
        charset = set()

        # We want the characters parameter to be a collection of characters or
        # character range. The method raises a `TypeError` each time there
        # is an issue.

        # case where it is not a collection
        if not isinstance(characters, list):
            raise TypeError(
                f"The characters parameter is of type: {type(characters)}. "
                "The characters parameter should be a list of characters or "
                "characters ranges. For example, "
                '[("A", "Z"), "é", "à", ("z", "b")] is a valid parameter. '
            )

        for elem in characters:

            if isinstance(elem, tuple):

                # check is the element is a valid character range
                try:
                    character_range = CharacterRange(elem)
                except TypeError as type_err:
                    raise type_err

                charset = charset.union(set(character_range.get_characters()))

            else:

                # the element is a valid character
                if _is_character(elem):
                    charset.add(elem)

                # the element is not character or character range
                else:
                    raise TypeError(
                        "The characters parameter contains an element that is not "
                        "a character or a character range. "
                        'For example, ("A", "Z"), "é", "à" or ("z", "b") are valid. '
                    )

        return charset

    def get_characters(self) -> Set[str]:
        """Returns the set of supported characters."""
        return self._characters

    def add_character(self, character: str) -> None:
        """
        Adds a character to the set of supported characters.

        The method returns a `TypeError` if the `character` parameter is
        is not valid.
        The `character` parameter should be a `str` of size 1.

        Parameters
        ----------
        character
            The character (`str` of size 1) to add.
        """
        if _is_character(character):
            self._characters.add(character)
        else:
            raise TypeError(
                f"{character} can't be added as it is not a character. "
                "It should be a `str` of length 1."
            )
