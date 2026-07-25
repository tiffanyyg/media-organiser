from pathlib import Path

from app.cleanup.screenshots import (
    is_screenshot,
)


IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".heic",
    ".webp",
}


def analyse_library(
    library: Path,
    large_file_size: int = 2_000_000_000,
):

    results = {
        "scanned": 0,
        "screenshots": [],
        "large_files": [],
    }


    for file in library.rglob("*"):

        if not file.is_file():
            continue


        results["scanned"] += 1


        if is_screenshot(file):

            results["screenshots"].append(
                file
            )


        if file.stat().st_size >= large_file_size:

            results["large_files"].append(
                file
            )


    return results

