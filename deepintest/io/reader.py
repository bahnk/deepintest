"""
Module to read files.
"""

from os import stat
from pathlib import Path
from typing import List


class TextFileReader:
    """\
    Class for reading files.

    TextFileReader is meant for reading streams of character only.
    It supports only UTF-8 and ASCII.

    This class doesn't assume that the default byte-buffer size is
    appropriate, so it includes a parameter to limit the file size.
    """

    _supported_encodings: List[str] = ["utf-8", "ascii"]
    _encoding: str
    _max_size: int
    _path: str

    def __init__(self, encoding: str = "utf-8", max_size: int = 2000000) -> None:
        """
        Constructor of the TextFileReader class.

        The constructor raises a `ValueError` if `encoding` is not a supported
        encoding.

        The constructor raises a `ValueError` if `max_size` is not an `int`.

        Parameters
        ----------
        encoding
            The file encoding.
        max_size
            The maximum size of a file to read in bytes.
        """
        if encoding not in self._supported_encodings:
            raise ValueError(f"{encoding} is not a supported encoding.")

        self._encoding = encoding

        if not isinstance(max_size, int):
            raise ValueError(f"max size {max_size} is not an int.")

        self._max_size = max_size

    @property
    def encoding(self) -> int:
        """Getter for _encoding."""
        return self._encoding

    @encoding.setter
    def encoding(self, new_encoding: int) -> None:
        """Setter for _encoding."""
        self._encoding = new_encoding

    @property
    def mem_size(self) -> int:
        """Getter for _mem_size."""
        return self._mem_size

    @mem_size.setter
    def mem_size(self, new_mem_size: int) -> None:
        """Setter for _mem_size."""
        self._mem_size = new_mem_size

    @property
    def path(self) -> int:
        """Getter for _path."""
        return self._path

    @path.setter
    def path(self, new_path: str) -> None:
        """Setter for _path."""
        self._path = new_path

    def read(self, path: str) -> List[str]:
        """\
        Reads the content of a file.

        If sucessful, the methods returns the content of the file as a `list`
        of `str`.

        The method will raise a:

            * `FileNotFoundError` if `path` doesn't exist
            * `ValueError` if `path` is a directory or a link
            * `MemoryError` if `path` size exceeds `max_size` parameter
            * `OSError` if `path` can't be opened
            * `UnicodeError` if the provided encoding can't decode the file

        Parameters
        ----------
        path
            The path of the file that needs to be read.
        """
        self._path = Path(path)

        # test for existence
        if not self._path.exists():
            raise FileNotFoundError(f"{self._path} doesn't exist.")

        # path can be a directory and decided not to handle links
        if not self._path.is_file() or self._path.is_symlink():
            raise ValueError(f"{self._path} points to a directory or a link.")

        # test if the file size exceeds the max_size
        if stat(self._path).st_size > self._max_size:
            raise MemoryError(f"{self._path} size exceeds the max_size parameter.")

        # check if the file can be opened
        try:
            with open(self._path, "rb") as file_obj:
                data = file_obj.read()
        except PermissionError as perm_err:
            raise perm_err
        except OSError as os_err:
            raise os_err

        # tests the encoding
        try:
            data.decode(encoding=self._encoding, errors="strict")
        except UnicodeError as uni_err:
            raise UnicodeError(
                f"{self._path} is not encoded with {self._encoding}."
            ) from uni_err

        # get the file content
        lines = []

        with open(self._path, "r", encoding=self._encoding) as file_obj:
            for line in file_obj.readlines():
                lines.append(line.rstrip())

        return lines
