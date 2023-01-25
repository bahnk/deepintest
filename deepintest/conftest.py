"""
Pytest configuration.
"""

import pytest


DEFAULT_ENCODING = "utf-8"
UNSUPPORTED_ENCODING = "utf-16"


@pytest.fixture(scope="package")
def default_encoding():
    """Returns the default supported encoding."""
    return DEFAULT_ENCODING


@pytest.fixture(scope="package")
def unsupported_encoding():
    """Returns an encoding that is not supported."""
    return UNSUPPORTED_ENCODING


@pytest.fixture(scope="package")
def not_char():
    """Returns a list of element that are not characters (str of size 1)."""
    return ["", "aa", ["a"], ("a"), ["a", "b"], {"one": 1}]


@pytest.fixture(scope="package")
def not_str():
    """Returns a list of element that are not str."""
    return [1, ["a"], ("a"), ["a", "b"], [1, 2], {"one": 1}]


@pytest.fixture(scope="package")
def not_str_list():
    """Returns a list of element that are not lists of str."""
    return ["", 1, "a", "aa", [1], ["a", 1]]
