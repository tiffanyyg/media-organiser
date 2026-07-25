from pathlib import Path

from app.importer.scanner import scan_directory
from app.duplicates.hasher import calculate_hash
from app.organizer.paths import build_media_path
from app.organizer.renamer import generate_filename
from app.organizer.mover import move_file
from app.metadata.extractor import extract_image_metadata


def import_media(
    inbox: Path,
    library: Path,
):
    files = scan_directory(inbox)

    imported = []

    for media in files:

        file_hash = calculate_hash(
            media.path
        )

        metadata = extract_image_metadata(
            media.path
        )

        if metadata.created_date:
            folder = build_media_path(
                library,
                metadata.created_date,
            )

        else:
            folder = library / "Unknown Date"

        filename = generate_filename(
            media.path,
            metadata.created_date,
        ) if metadata.created_date else media.path.name


        destination = folder / filename

        move_file(
            media.path,
            destination,
        )

        imported.append(destination)

    return imported

