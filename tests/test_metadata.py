from pathlib import Path

from PIL import Image

from app.metadata.extractor import extract_image_metadata


def test_extract_basic_metadata(tmp_path):
    image_path = tmp_path / "test.jpg"

    image = Image.new(
        "RGB",
        (100, 200)
    )

    image.save(image_path)

    metadata = extract_image_metadata(image_path)

    assert metadata.width == 100
    assert metadata.height == 200

