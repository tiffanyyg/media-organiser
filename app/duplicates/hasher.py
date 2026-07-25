import hashlib
from pathlib import Path


def calculate_hash(
    file_path: Path,
    chunk_size: int = 1024 * 1024,
) -> str:
    """
    Calculate SHA-256 hash of a file.

    Files are read in chunks so large videos
    do not consume large amounts of memory.
    """

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(chunk_size):
            sha256.update(chunk)

    return sha256.hexdigest()

