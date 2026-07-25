from pathlib import Path
import hashlib



def calculate_hash(
    file_path: Path,
    chunk_size: int = 8192,
) -> str:
    """
    Calculate SHA256 hash for a file.
    """

    sha256 = hashlib.sha256()


    with file_path.open(
        "rb"
    ) as file:

        while chunk := file.read(
            chunk_size
        ):

            sha256.update(
                chunk
            )


    return sha256.hexdigest()



def hash_file(
    file_path: Path,
    chunk_size: int = 8192,
) -> str:
    """
    Alias for calculate_hash.

    Kept for newer duplicate manager code.
    """

    return calculate_hash(
        file_path,
        chunk_size,
    )

