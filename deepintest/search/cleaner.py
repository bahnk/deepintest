"""
Cleaner module to remove unwanted characters from strings.
"""

import re

from deepintest._conf import default_characters
from deepintest._typing import Chars

from .characters import CharacterSet


class Cleaner:
    """
    Class to removes unwanted characters from a string.
    """

    _charset: CharacterSet
    _delimiter: str

    def __init__(self, characters: Chars = None, delimiter: str = " ") -> None:
        """\
        Constructor of the Cleaner class.

        The constructor returns a `TypeError` if the `characters` parameter is
        is not valid.
        The `characters` parameter should be a `list` of characters
        (`str` of size 1) and/or `tuple` of characters.
        For example, `["A", ("B", "E"), "g", ("z", "v")]` is valid.

        The constructor returns a `TypeError` if the `delimiter` parameter is
        is not valid.
        The `delimiter` parameter should be a character (`str` of size 1).

        Parameters
        ----------
        characters
            A `list` of characters (`str` of size 1) and/or `tuple` of characters.
            That we want to keep in the stringself.
            Any other character is removed.
            For example, `["A", ("B", "E"), "g", ("z", "v")]` is valid.
        delimiter
            Character (`str` of size 1) used to separated the words in a string.
            It is usually a space (" ").
        """
        # delimiter should be a single character not several character
        if isinstance(delimiter, str) and len(delimiter) == 1:
            self._delimiter = delimiter
        else:
            raise TypeError(
                "The delimiter parameter is not a character. "
                "It should be a `str` of length 1."
            )

        # set up supported characters
        if characters:
            try:
                self._charset = CharacterSet(characters)
            except TypeError as type_err:
                raise type_err
        else:
            try:
                self._charset = CharacterSet(default_characters)
            except TypeError as type_err:
                raise type_err

        # adds the delimiter to the supported characters
        try:
            self._charset.add_character(self._delimiter)
        except TypeError as type_err:
            raise type_err


    @property
    def charsest(self):
        """Getter for character set."""
        return self._charset

    def clean_line(self, line: str) -> str:
        """\
        Removes the unsupported characters and extra delimiter from a string.

        The method returns a `str`.

        The method returns a `TypeError` if the `line` parameter is not a `str`.

        Parameters
        ----------
        line
            Line to clean as a `str`.
        """
        if not isinstance(line, str):
            raise TypeError(
                "The line parameter should be a str. "
                f"Here is the problematic line: {line}"
            )

        new_line = ""

        # remove unsupported characters
        for character in line:
            if character in self._charset:
                new_line += character
            else:
                new_line += self._delimiter

        # remove extra spaces
        new_line = re.sub(f"^{self._delimiter}+", "", new_line)
        new_line = re.sub(f"{self._delimiter}+$", "", new_line)
        new_line = re.sub(f"{self._delimiter}+", self._delimiter, new_line)

        return new_line
