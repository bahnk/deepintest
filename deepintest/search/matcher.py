"""
Module to search for a term in a string.
"""


class Matcher:
    """
    Class to search for a term in a string.
    """

    _search_term: str

    def __init__(self, search_term: str) -> None:
        """\
        Constructor of the Matcher class.

        The constructor raises a `TypeError` the `search_term` parameter is not
        a `str`.

        The constructor raises a `ValueError` the `search_term` parameter is an
        empty `str` or contains spaces.

        Parameters
        ----------
        search_term
            The term to search.
        """
        if isinstance(search_term, str):
            if len(search_term) > 0:
                if search_term.find(" ") < 0:
                    self._search_term = search_term
                else:
                    raise ValueError("The search_term parameter contains spaces.")
            else:
                raise ValueError("The search_term parameter is an empty str.")
        else:
            raise TypeError(
                f"The search_term parameter is of type: {type(search_term)}. "
                "The search_term parameter should be a str."
            )

    @property
    def search_term(self):
        """Getter for search term."""
        return self._search_term

    def match(self, line: str) -> bool:
        """
        This method returns True is the search term is a substring of the line.

        The constructor returns a `TypeError` the `line` parameter is not a `str`.

        Parameters
        ----------
        line
            The string to search in.
        """
        if not isinstance(line, str):
            raise TypeError("The line parameter is not a str.")

        return line.find(self._search_term) > -1
