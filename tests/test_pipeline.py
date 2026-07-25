from pathlib import Path

from app.importer.pipeline import import_media


def test_import_pipeline(tmp_path):

    inbox = tmp_path / "inbox"
    library = tmp_path / "library"

    inbox.mkdir()

    photo = inbox / "photo.jpg"
    photo.write_text("test")

    results = import_media(
        inbox,
        library,
    )

    assert len(results) == 1
    assert results[0].exists()

