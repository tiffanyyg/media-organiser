from pathlib import Path

from app.duplicates.hasher import calculate_hash
from app.duplicates.detector import find_duplicates


def test_same_file_has_same_hash(tmp_path):
    file = tmp_path / "photo.jpg"

    file.write_text("hello")

    first = calculate_hash(file)
    second = calculate_hash(file)

    assert first == second


def test_duplicate_detection(tmp_path):
    first = tmp_path / "one.jpg"
    second = tmp_path / "two.jpg"

    first.write_text("same photo")
    second.write_text("same photo")

    duplicates = find_duplicates(
        [
            first,
            second,
        ]
    )

    assert len(duplicates) == 1

