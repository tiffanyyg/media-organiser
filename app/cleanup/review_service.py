from pathlib import Path

from app.cleanup.analyser import analyse_library
from app.cleanup.reviewer import move_to_review



def run_review(
    library: Path,
    review_root: Path,
):

    results = analyse_library(
        library
    )


    moved = {
        "screenshots": [],
        "large_files": [],
    }


    moved["screenshots"] = move_to_review(
        results["screenshots"],
        review_root / "screenshots",
    )


    moved["large_files"] = move_to_review(
        results["large_files"],
        review_root / "large-files",
    )


    return moved

