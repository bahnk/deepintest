"""
Solution to Deeper Insights coding test.
"""

# coding: utf-8

import re
import sys
import click

from deepintest.io.reader import TextFileReader
from deepintest.search.cleaner import Cleaner
from deepintest.search.matcher import Matcher
from deepintest.io.formatter import Formatter


def solution(path, max_size=int(1e9)):
    """
    Reads a file, extracts the search term then print the clean matched lines.
    """

    reader = TextFileReader(max_size=max_size)

    try:
        file_content = reader.read(path)
    except FileNotFoundError:
        print(f"Error: {path} doesn't exist")
        sys.exit(1)
    except MemoryError:
        print(f"Error: {path} size is too big")
        print("Please consider using the --max-size option")
        print("Run `solution --help` for more information")
        sys.exit(1)
    except PermissionError:
        print(f"Error: {path} doesn't have adequate right access")
        sys.exit(1)
    except OSError:
        print(f"Error: {path} exists but can't be opened")
        sys.exit(1)
    except UnicodeError:
        print(f"Error: {path} is not encoded with UTF-8")
        sys.exit(1)
    except ValueError:
        print(f"Error: {path} is a directory or a link")
        sys.exit(1)

    # search term can't match empty lines, or lines with only spaces, so we can
    # remove all of them
    file_content = list(filter(lambda x: len(re.sub(" ", "", x))>0, file_content))

    # empty file or with only empty lines
    if len(file_content) == 0:
        print(f"Error: {path} is empty or has only empty lines or lines with spaces")
        sys.exit(1)

    # must have at least a line and a search term
    if len(file_content) < 2:
        print("Error: file must contain at least two lines (a line and a term)")
        sys.exit(1)

    # we extract the search term and the lines to match
    search_term = file_content[-1]
    lines = file_content[:-1]

    if len(search_term.split(" ")) != 1:
        print("Error: search term should be a word (string without spaces)")
        sys.exit(1)

    # we filter the lines containing the search term
    matcher = Matcher(search_term=search_term)
    matched_lines = [line for line in lines if matcher.match(line)]

    # we specify allowed characters
    characters = [("A", "Z"), ("a", "z"), ("À", "Ö"), ("Ø", "ʯ"), "ù", "ú"]
    cleaner = Cleaner(characters=characters)

    # this will format the output
    formatter = Formatter()

    # we print the outptut
    for line in matched_lines:
        print(formatter.format_line(cleaner.clean_line(line)))

# pylint: disable=no-value-for-parameter
@click.command()
@click.option('--max-size', default=int(1e9), help='maximum file size in bytes')
@click.argument("path")
def main(max_size, path):
    """
    Solution to Deeper Insights Coding Test.

    This script takes the path (`PATH`) of a file as argument. Then, it reads
    the file, extracts the search term and print the clean matched lines.
    """
    solution(path, max_size)

if __name__ == "__main__":
    main()
