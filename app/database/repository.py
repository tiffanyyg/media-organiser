from datetime import datetime

from app.database.database import SessionLocal
from app.database.models import MediaRecord


def save_media(
    filename: str,
    original_filename: str,
    path: str,
    file_hash: str,
    media_type: str,
):

    session = SessionLocal()

    record = MediaRecord(
        filename=filename,
        original_filename=original_filename,
        path=path,
        file_hash=file_hash,
        media_type=media_type,
        imported_at=datetime.now(),
    )

    session.add(record)

    session.commit()

    session.close()

def find_by_hash(file_hash: str):

    session = SessionLocal()

    record = (
        session.query(MediaRecord)
        .filter(
            MediaRecord.file_hash == file_hash
        )
        .first()
    )

    session.close()

    return record

