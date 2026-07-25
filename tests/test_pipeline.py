from app.database.database import engine
from app.database.models import Base

from app.importer.pipeline import import_media


def test_import_pipeline(tmp_path):

    Base.metadata.drop_all(
        engine
    )

    Base.metadata.create_all(
        engine
    )


    inbox = tmp_path / "inbox"

    library = tmp_path / "library"


    inbox.mkdir()


    photo = inbox / "photo.jpg"


    photo.write_text(
        "test"
    )


    report = import_media(
        inbox,
        library,
    )


    assert report.imported_count == 1

    assert report.duplicate_count == 0

    assert report.error_count == 0

    assert report.imported[0].exists()

