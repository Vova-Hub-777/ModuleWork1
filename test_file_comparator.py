import pytest
from main import read_file, write_file


@pytest.fixture
def sample_files(tmpdir):
    file1 = tmpdir.join("file1.txt")
    file2 = tmpdir.join("file2.txt")

    file1.write("Line 1\nLine 2\nLine 3\n")
    file2.write("Line 2\nLine 3\nLine 4\n")

    return str(file1), str(file2)

def test_read_file(sample_files):
    file1, file2 = sample_files
    file1_content = read_file(file1)
    file2_content = read_file(file2)

    assert file1_content == ["Line 1\n", "Line 2\n", "Line 3\n"]
    assert file2_content == ["Line 2\n", "Line 3\n", "Line 4\n"]


@pytest.mark.parametrize("file_name", ["non_existent.txt", "another_non_existent.txt"])
def test_read_file_not_found(file_name, capsys):
    read_file(file_name)
    captured = capsys.readouterr()

    assert captured.out == f"File {file_name} was not found.\n"

def test_write_file(tmpdir):
    file_name = str(tmpdir.join("output.txt"))
    content = ["Line 1\n", "Line 2\n"]

    write_file(file_name, content)

    with open(file_name, "r") as file:
        written_content = file.readlines()

    assert written_content == content