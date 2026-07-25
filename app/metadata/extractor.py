from pathlib import Path

from PIL import Image, ExifTags

from app.core.models import MediaMetadata


def extract_image_metadata(path: Path) -> MediaMetadata:
    metadata = MediaMetadata(
        path=path
    )

    try:
        with Image.open(path) as image:
            metadata.width, metadata.height = image.size

            exif = image.getexif()

            for key, value in exif.items():
                tag = ExifTags.TAGS.get(key)

                if tag == "Model":
                    metadata.camera = str(value)

                if tag == "DateTimeOriginal":
                    metadata.created_date = value

    except Exception:
        pass

    return metadata

