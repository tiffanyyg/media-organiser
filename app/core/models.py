from dataclasses import dataclass
from pathlib import Path
from datetime import datetime


@dataclass
class MediaFile:
    path: Path
    media_type: str


@dataclass
class MediaMetadata:
    path: Path
    created_date: datetime | None = None
    camera: str | None = None
    width: int | None = None
    height: int | None = None
    latitude: float | None = None
    longitude: float | None = None

