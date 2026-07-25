from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class MediaRecord(Base):
    __tablename__ = "media"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    filename: Mapped[str]

    path: Mapped[str]

    file_hash: Mapped[str]

    media_type: Mapped[str]

