from sqlalchemy import select

from app.database.database import SessionLocal
from app.database.models import MediaRecord



def search_filename(
    keyword: str,
):
    """
    Search media by filename.
    """

    session = SessionLocal()

    try:

        query = select(
            MediaRecord
        ).where(
            MediaRecord.filename.contains(
                keyword
            )
        )


        results = session.execute(
            query
        )


        return results.scalars().all()


    finally:

        session.close()



def search_type(
    media_type: str,
):
    """
    Search media by type.
    """

    session = SessionLocal()

    try:

        query = select(
            MediaRecord
        ).where(
            MediaRecord.media_type == media_type
        )


        results = session.execute(
            query
        )


        return results.scalars().all()


    finally:

        session.close()

