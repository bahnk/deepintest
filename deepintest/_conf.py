"""
Default Configuration variables.
"""

from deepintest._typing import Chars

# the default supported characters
default_characters: Chars = [
    # upper and lower case
    ("A", "Z"),
    ("a", "z"),
    # example of accents and other characters of the LATIN charset
    ("À", "Ö"),
    ("Ø", "ʯ"),
    # to illustrate it can take single values
    "ù",
    "ú",
    "û",
]
