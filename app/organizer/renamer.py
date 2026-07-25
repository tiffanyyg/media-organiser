from datetime import datetime
from pathlib import Path


def generate_filename(
    original: Path,
    date_taken: datetime,
) -> str:
    """
    Generate a consistent filename.
    """

    timestamp = date_taken.strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    return f"{timestamp}{original.suffix.lower()}"

