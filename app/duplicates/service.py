from pathlib import Path

from app.duplicates.manager import (
    find_duplicate_groups,
    select_duplicates,
)

from app.duplicates.report import (
    generate_duplicate_report,
)

from app.cleanup.reviewer import (
    move_to_review,
)



def run_duplicate_review(
    library: Path,
    review_folder: Path,
    report_folder: Path,
):


    groups = find_duplicate_groups(
        library
    )


    report = generate_duplicate_report(
        groups
    )


    report_folder.mkdir(
        parents=True,
        exist_ok=True,
    )


    report_file = (
        report_folder /
        "duplicate_report.txt"
    )


    report_file.write_text(
        report
    )


    duplicates = select_duplicates(
        groups
    )


    moved = move_to_review(
        duplicates,
        review_folder,
    )


    return {
        "groups": groups,
        "moved": moved,
        "report": report,
    }

