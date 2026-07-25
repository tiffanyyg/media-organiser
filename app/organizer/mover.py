from pathlib import Path
import shutil


def move_file(
    source: Path,
    destination: Path,
) -> Path:
    """
    Move a file safely.

    Creates destination folders if needed.
    """

    destination.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    shutil.copy2(
        source,
        destination,
    )

    return destination

