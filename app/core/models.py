from dataclasses import dataclass
from pathlib import Path


@dataclass
class MediaFile:
    path: Path
    media_type: str

