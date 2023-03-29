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