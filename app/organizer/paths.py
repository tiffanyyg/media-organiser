from datetime import datetime
from pathlib import Path


MONTH_NAMES = [
    "",
    "01 - January",
    "02 - February",
    "03 - March",
    "04 - April",
    "05 - May",
    "06 - June",
    "07 - July",
    "08 - August",
    "09 - September",
    "10 - October",
    "11 - November",
    "12 - December",
]


def build_media_path(
    library_root: Path,
    date_taken: datetime,
) -> Path:
    """
    Create Year/Month folder structure.
    """

    return (
        library_root
        / str(date_taken.year)
        / MONTH_NAMES[date_taken.month]
    )

