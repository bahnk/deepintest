"""
Testing module for the deepingtest.io.reader module.
"""


from typing import List
import pytest
from ..reader import TextFileReader


class TestTextFileReader:
    """The test class associated with the TextFileReader class."""

    def _create_test_file_from_lines(
        self, path: str, lines: List[str], encoding: str = "utf-8"
    ) -> None:
        """Create a test file containing the lines passed as parameter."""
        with open(path, "w", encoding=encoding) as file_obj:
            for line in lines:
                file_obj.write(f"{line}\n")

    def test_constructor_fails_when_max_size_not_int(self):
        """
        Tests if the constructor returns a `ValueError` when the provided
        encoding is not supported.
        """
        tests = ["a", "aa", [1], {"one": 1}]
        with pytest.raises(ValueError):
            for elem in tests:
                TextFileReader(max_size=elem)

    def test_constructor_fails_when_encoding_not_supported(self, unsupported_encoding):
        """
        Tests if the constructor returns a `ValueError` when the provided
        encoding is not supported.
        """
        with pytest.raises(ValueError):
            TextFileReader(encoding=unsupported_encoding)

    def test_read_fails_when_path_not_exist(self, tmp_path):
        """
        Tests if TextFileReader.read returns a `FileNotFoundError` when the
        provided path doesn't exist.
        """
        text_file_reader = TextFileReader()
        with pytest.raises(FileNotFoundError):
            text_file_reader.read(tmp_path / "file")

    def test_read_fails_when_path_is_directory(self, tmp_path):
        """
        Tests if TextFileReader.read returns a `ValueError` when the provided
        path is a directory.
        """
        text_file_reader = TextFileReader()
        with pytest.raises(ValueError):
            text_file_reader.read(tmp_path)

    def test_read_fails_when_path_is_symlink(self, tmp_path, default_encoding):
        """
        Tests if TextFileReader.read returns a `ValueError` when the provided
        path is a symbolic link.
        """
        src = tmp_path / "src"
        dst = tmp_path / "dst"
        with src.open("w", encoding=default_encoding):
            pass
        dst.symlink_to(src)
        text_file_reader = TextFileReader()
        with pytest.raises(ValueError):
            text_file_reader.read(dst)

    def test_read_fails_when_file_size_too_large(self, tmp_path):
        """
        Tests if TextFileReader.read returns MemoryError when the provided
        path points to a file whose size exceeds max_size.
        """
        size = 10
        path = tmp_path / "file"
        with open(path, "wb") as file_obj:
            for _ in range(size):
                file_obj.write(b"\x00")
        text_file_reader = TextFileReader(max_size=size-1)
        with pytest.raises(MemoryError):
            text_file_reader.read(path)

    def test_read_fails_when_file_has_unsupported_encoding(
            self,
            tmp_path,
            unsupported_encoding
        ):
        """
        Tests if TextFileReader.read return an `UnicodeError` when the provided
        path points to a file with a non supported encoding.
        """
        path = tmp_path / "file"
        with open(path, "w", encoding=unsupported_encoding) as file_obj:
            for i in range(1, 5):
                file_obj.write(f"line {i}\n")
        text_file_reader = TextFileReader()
        with pytest.raises(UnicodeError):
            text_file_reader.read(path)

    def test_read_returns_file_content_as_list(self, tmp_path) -> bool:
        """
        Tests if TextFileReader.read returns the file content as list of
        strings.
        """
        path = tmp_path / "file"
        lines = ["line1", "line2", "line3"]
        self._create_test_file_from_lines(path, lines)
        text_file_reader = TextFileReader()
        content = text_file_reader.read(path)
        assert content == lines
