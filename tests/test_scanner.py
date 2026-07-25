from pathlib import Path

from app.importer.scanner import scan_directory


def test_scanner_finds_media(tmp_path):
    image = tmp_path / "photo.jpg"
    video = tmp_path / "video.mov"
    text = tmp_path / "file.txt"

    image.touch()
    video.touch()
    text.touch()

    results = scan_directory(tmp_path)

    assert len(results) == 2

