from datetime import datetime
from pathlib import Path

from app.organizer.paths import build_media_path
from app.organizer.renamer import generate_filename


def test_build_media_path(tmp_path):
    result = build_media_path(
        tmp_path,
        datetime(2024, 7, 18)
    )

    assert result.name == "07 - July"
    assert result.parent.name == "2024"


def test_generate_filename():
    filename = generate_filename(
        Path("IMG_1234.JPG"),
        datetime(2024, 7, 18, 14, 30, 5)
    )

    assert filename == (
        "2024-07-18_14-30-05.jpg"
    )

