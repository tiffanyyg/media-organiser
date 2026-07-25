from pathlib import Path

from app.duplicates.hasher import hash_file


def find_duplicate_groups(
    library: Path,
):

    hashes = {}


    for file in library.rglob("*"):

        if not file.is_file():
            continue


        file_hash = hash_file(
            file
        )


        if file_hash not in hashes:

            hashes[file_hash] = []


        hashes[file_hash].append(
            file
        )


    duplicates = []


    for files in hashes.values():

        if len(files) > 1:

            duplicates.append(
                files
            )


    return duplicates



def select_duplicates(
    groups: list[list[Path]],
):

    duplicates = []


    for group in groups:

        # keep first file
        # move remaining copies

        duplicates.extend(
            group[1:]
        )


    return duplicates

