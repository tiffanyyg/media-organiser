from pathlib import Path

from app.duplicates.hasher import calculate_hash


def find_duplicates(files: list[Path]) -> dict[str, list[Path]]:
    """
    Group files by identical hash.
    """

    hashes = {}

    for file in files:
        file_hash = calculate_hash(file)

        if file_hash not in hashes:
            hashes[file_hash] = []

        hashes[file_hash].append(file)

    return {
        file_hash: paths
        for file_hash, paths in hashes.items()
        if len(paths) > 1
    }

