from pathlib import Path

from app.database.repository import save_media
from app.duplicates.hasher import calculate_hash
from app.importer.scanner import scan_directory
from app.metadata.extractor import extract_image_metadata
from app.organizer.mover import move_file
from app.organizer.paths import build_media_path
from app.organizer.renamer import generate_filename


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

        if metadata.created_date:
            filename = generate_filename(
                media.path,
                metadata.created_date,
            )
        else:
            filename = media.path.name

        destination = folder / filename

        move_file(
            media.path,
            destination,
        )

        save_media(
            filename=destination.name,
            original_filename=media.path.name,
            path=str(destination),
            file_hash=file_hash,
            media_type=media.media_type,
        )

        imported.append(destination)

    return imported

