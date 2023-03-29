import pytest
from main import read_file, write_file


@pytest.fixture
def sample_files(tmpdir):
    file1 = tmpdir.join("file1.txt")
    file2 = tmpdir.join("file2.txt")

    file1.write("Line 1\nLine 2\nLine 3\n")
    file2.write("Line 2\nLine 3\nLine 4\n")

    return str(file1), str(file2)