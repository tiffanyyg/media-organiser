from pathlib import Path

from app.core.models import MediaFile


IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".heic",
    ".webp",
    ".raw",
}

VIDEO_EXTENSIONS = {
    ".mov",
    ".mp4",
    ".avi",
    ".mkv",
}


def scan_directory(directory: Path) -> list[MediaFile]:
    files = []

    for file in directory.rglob("*"):
        if not file.is_file():
            continue

        extension = file.suffix.lower()

        if extension in IMAGE_EXTENSIONS:
            files.append(
                MediaFile(
                    path=file,
                    media_type="image",
                )
            )

        elif extension in VIDEO_EXTENSIONS:
            files.append(
                MediaFile(
                    path=file,
                    media_type="video",
                )
            )

    return files

