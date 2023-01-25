"""
Module to format outputs.
"""

from typing import List

from deepintest._utils import _is_character


class Formatter:
    """
    Class to format the output of a list of lines.
    """

    _input_delimiter: str
    _output_delimiter: str
    _left_border: str
    _right_border: str

    def __init__(
        self,
        input_delimiter: str = " ",
        output_delimiter: str = " ",
        left_border: str = "[",
        right_border: str = "]",
    ):
        """\
        Constructor of the Formatter class.

        The constructor raises a `TypeError` if `input_delimiter`,
        `output_delimiter`, `left_border`, or `right_border` are not characters.

        Parameters
        ----------
        input_delimiter
            Character that separates the words in the input lines.
        output_delimiter
            Character that separates the words in the output lines.
        left_border
            Character the output line starts with.
        right_border
            Character the output line ends with.
        """
        # pylint: disable=unused-argument
        for attr_name, attr_value in locals().items():
            if attr_name == "self":
                continue
            if _is_character(attr_value):
                setattr(self, f"_{attr_name}", attr_value)
            else:
                raise TypeError(
                    f"{attr_value} is not a valid {attr_name}. "
                    "It should be a character."
                )

    def format_line(self, line: str) -> str:
        """\
        Format a line with delimiter and borders.

        The methods returns a formatted `str` or raises a `TypeError` if the
        `line` parameter is not a `str`.

        Parameters
        ----------
        line
            `str` to format.
        """
        if not isinstance(line, str):
            raise TypeError(
                f"The line parameter is of type: {type(line)}. "
                "The line parameter should be str."
            )

        words = line.split(self._input_delimiter)

        new_line = f"{self._left_border}"
        new_line = new_line + f"{self._output_delimiter.join(words)}"
        new_line = new_line + f"{self._right_border}"

        return new_line

    def format_lines(self, lines: List[str]):
        """\
        Format a list of lines with delimiter and borders.

        The methods returns `str` of formatted lines separated by a new line
        character.

        The method returns a `TypeError` if the `lines` parameter is not
        a `list` or if one element of that list is not a `str`.

        Parameters
        ----------
        lines
            A list of `str` to format.
        """
        new_lines = []

        for line in lines:
            new_lines.append(self.format_line(line))

        return "\n".join(new_lines)
