import pytest
import os
from src.monitor import FileChangeHandler


@pytest.fixture
def revision_files(tmp_path):
    last_revision_file = tmp_path / "last_revision.txt"
    last_revision_file.write_text("line1\nline2\nline3\n")

    current_revision_file = tmp_path / "current_revision.txt"
    current_revision_file.write_text("line3\nline2\nline1\n")

    return str(last_revision_file), str(current_revision_file)


def test_compare_revisions(tmp_path):
    last_revision_file = tmp_path / "last_revision.txt"
    last_revision_file.write_text("line1\nline2\nline3\n")

    current_revision_file = tmp_path / "current_revision.txt"
    current_revision_file.write_text("line3\nline2\nline1\n")

    file_path = "revision.txt"
    temp_dir = tmp_path

    handler = FileChangeHandler(
        files_to_monitor=[],
        config_file="config_file",
        store_temp=True,
        temp_dir=str(tmp_path),
    )

    # Replace this part with how your class handles the paths
    handler.last_revision_path = str(last_revision_file)
    handler.current_revision_path = str(current_revision_file)

    changes = handler.compare_revisions(file_path)

    expected_changes = [
        ("line3", "line1"),  # modified line
        ("line1", "line3"),  # modified line
    ]

    assert changes == expected_changes
