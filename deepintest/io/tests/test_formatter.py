"""
Testing module for the deepingtest.io.formatter module.
"""


import pytest
from ..formatter import Formatter


class TestFormatter:
    """The test class associated with the Formatter class."""

    def test_constructor_fails_when_parameters_are_wrong_type(self, not_char):
        """
        Tests if Formatter's constructor returns a `TypeError` when the
        parameters are not characters (str of size 1).
        """
        with pytest.raises(TypeError):
            for elem in not_char:
                Formatter(input_delimiter=elem)
                Formatter(output_delimiter=elem)
                Formatter(left_border=elem)
                Formatter(right_border=elem)

    def test_format_line_fails_when_parameter_is_wrong_type(self, not_str):
        """
        Tests if Formatter.format_line returns a `TypeError` the line parameter
        is not a str.
        """
        formatter = Formatter()
        with pytest.raises(TypeError):
            for elem in not_str:
                formatter.format_line(elem)

    def test_format_line_returns_proper_result(self):
        """
        Tests the result of Formatter.format_line.
        """
        tests = [("a,b,c", "<a:b:c>"), ("ab,cd,ef", "<ab:cd:ef>")]
        args = {
            "input_delimiter": ",",
            "output_delimiter": ":",
            "left_border": "<",
            "right_border": ">",
        }
        formatter = Formatter(**args)
        for line, result in tests:
            assert formatter.format_line(line) == result

    def test_format_lines_fails_when_parameter_is_wrong_type(self, not_str_list):
        """
        Tests if Formatter.format_lines returns a `TypeError` the lines
        parameter is not a list of str.
        """
        formatter = Formatter()
        with pytest.raises(TypeError):
            for elem in not_str_list:
                formatter.format_lines(elem)

    def test_format_lines_returns_proper_result(self):
        """
        Tests the result of Formatter.format_lines.
        """
        tests = [(["a,b,c", "ab,cd,ef"], "<a:b:c>\n<ab:cd:ef>")]
        args = {
            "input_delimiter": ",",
            "output_delimiter": ":",
            "left_border": "<",
            "right_border": ">",
        }
        formatter = Formatter(**args)
        for lines, result in tests:
            assert formatter.format_lines(lines) == result
