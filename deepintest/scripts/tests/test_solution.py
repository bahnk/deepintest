"""
Testing module for the solution script.
"""

from os.path import dirname, join

import pytest

from .. solution import solution


def _read_file(path):
    """Returns the content of a file as a str."""
    with open(path, encoding="utf-8") as file_obj:
        return file_obj.read()


def test_read_fails_when_path_not_exist(capsys, tmp_path):
    """
    Tests if solution returns exit code 1 the expected output when the file
    doesn't exist.
    """
    path = tmp_path / "file"

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        solution(path)

    assert pytest_wrapped_e.value.code == 1
    assert pytest_wrapped_e.type == SystemExit

    captured = capsys.readouterr()
    assert captured.out == f"Error: {path} doesn't exist\n"


def test_read_fails_when_path_is_directory(capsys, tmp_path):
    """
    Tests if solution returns exit code 1 the expected output when it was given
    a directory.
    """
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        solution(tmp_path)

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1

    captured = capsys.readouterr()
    assert captured.out == f"Error: {tmp_path} is a directory or a link\n"


def test_read_fails_when_path_is_symlink(capsys, tmp_path):
    """
    Tests if solution returns exit code 1 the expected output when it was given
    a symbolic link.
    """
    src = tmp_path / "src"
    dst = tmp_path / "dst"

    with src.open("wb"):
        pass

    dst.symlink_to(str(src))

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        solution(dst)

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1

    captured = capsys.readouterr()
    assert captured.out == f"Error: {dst} is a directory or a link\n"


def test_read_fails_when_file_size_too_large(capsys, tmp_path):
    """
    Tests if solution returns exit code 1 the expected output when it was given
    path pointing to a file whose size exceeds max_size.
    """
    size = 20
    path = tmp_path / "file"

    with open(path, "wb") as file_obj:
        for _ in range(size):
            file_obj.write(b"\x00")

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        solution(path, size-1)

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1

    out_lines = [
        f"Error: {path} size is too big",
        "Please consider using the --max-size option",
        "Run `solution --help` for more information"
    ]
    captured = capsys.readouterr()
    assert captured.out == "\n".join(out_lines) + "\n"


def test_read_fails_when_file_has_unsupported_encoding(
        capsys,
        tmp_path,
        unsupported_encoding
    ):
    """
    Tests if solution returns exit code 1 the expected output when it was given
    path pointing to a file whose encoding is not supported.
    """
    path = tmp_path / "file"

    with open(path, "w", encoding=unsupported_encoding) as file_obj:
        for i in range(1, 10):
            file_obj.write(f"line {i}\n")

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        solution(path)

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1

    captured = capsys.readouterr()
    assert captured.out == f"Error: {path} is not encoded with UTF-8\n"


def test_read_fails_when_file_is_empty(capsys, tmp_path, default_encoding):
    """
    Tests if solution returns exit code 1 the expected output when it was given
    path pointing to an empty file.
    """
    path = tmp_path / "file"

    with open(path, "w", encoding=default_encoding):
        pass

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        solution(path)

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1

    captured = capsys.readouterr()
    assert captured.out == f"Error: {path} is empty or has only empty lines or lines with spaces\n"


def test_read_fails_when_file_is_empty_lines(capsys, tmp_path, default_encoding):
    """
    Tests if solution returns exit code 1 the expected output when it was given
    path pointing to a file containing only empty lines.
    """
    path = tmp_path / "file"

    with open(path, "w", encoding=default_encoding) as file_obj:
        file_obj.writelines(["\n"] * 5 + ["  \n"] * 5)

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        solution(path)

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1

    captured = capsys.readouterr()
    assert captured.out == f"Error: {path} is empty or has only empty lines or lines with spaces\n"


def test_read_fails_when_file_not_enough_lines(capsys, tmp_path, default_encoding):
    """
    Tests if solution returns exit code 1 the expected output when it was given
    path pointing to an empty file.
    """
    path = tmp_path / "file"

    with open(path, "w", encoding=default_encoding) as file_obj:
        file_obj.write("line\n")

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        solution(path)

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1

    captured = capsys.readouterr()
    assert captured.out == "Error: file must contain at least two lines (a line and a term)\n"


def test_read_fails_when_search_term_not_a_word(capsys, tmp_path, default_encoding):
    """
    Tests if solution returns exit code 1 the expected output when it was given
    a search term that is not a word.
    """
    path = tmp_path / "file"

    with open(path, "w", encoding=default_encoding) as file_obj:
        file_obj.writelines(["word1 word2\n", "word3 word4\n"])

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        solution(path)

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1

    captured = capsys.readouterr()
    assert captured.out == "Error: search term should be a word (string without spaces)\n"


def test_solution(capsys):
    """Tests if solution returns the expected result."""
    root_dir = join(dirname(__file__), "examples")
    tests = [
        ("example1.txt", "result1.txt"),
        ("example2.txt", "result2.txt"),
        ("example3.txt", "result3.txt"),
        ("example4.txt", "result4.txt"),
        ("example5.txt", "result5.txt")
    ]
    for example, result in tests:
        solution(join(root_dir, example))
        captured = capsys.readouterr()
        assert captured.out == _read_file(join(root_dir, result))
