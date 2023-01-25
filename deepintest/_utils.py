"""
Utilities functions.
"""

def _is_character(character):
    """Returns True if the argument is a str of size 1."""
    return isinstance(character, str) and len(character) == 1
