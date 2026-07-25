from pathlib import Path
import shutil


def move_to_review(
    files: list[Path],
    review_folder: Path,
):
    """
    Move files into a review folder.
    """

    moved = []


    review_folder.mkdir(
        parents=True,
        exist_ok=True,
    )


    for file in files:

        if not file.exists():
            continue


        destination = (
            review_folder /
            file.name
        )


        counter = 1

        while destination.exists():

            destination = (
                review_folder /
                f"{file.stem}_{counter}{file.suffix}"
            )

            counter += 1


        shutil.move(
            str(file),
            str(destination),
        )


        moved.append(
            destination
        )


    return moved

