from app.database.database import SessionLocal
from app.database.models import MediaRecord


def save_media(
    filename: str,
    path: str,
    file_hash: str,
    media_type: str,
):
    session = SessionLocal()

    record = MediaRecord(
        filename=filename,
        path=path,
        file_hash=file_hash,
        media_type=media_type,
    )

    session.add(record)
    session.commit()
    session.close()

