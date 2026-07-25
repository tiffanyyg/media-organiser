from pathlib import Path

from app.cleanup.analyser import analyse_library
from app.cleanup.screenshots import is_screenshot


def test_detect_screenshot():

    file = Path(
        "Screenshot 2026.png"
    )

    assert is_screenshot(file)


def test_cleanup_analysis(tmp_path):

    library = tmp_path / "library"

    library.mkdir()


    photo = library / "holiday.jpg"

    photo.write_text(
        "photo"
    )


    screenshot = (
        library /
        "Screenshot 1.png"
    )

    screenshot.write_text(
        "screen"
    )


    results = analyse_library(
        library
    )


    assert results["scanned"] == 2

    assert len(
        results["screenshots"]
    ) == 1

