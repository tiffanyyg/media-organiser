from pathlib import Path

from app.cleanup.analyser import analyse_library
from app.cleanup.report import generate_cleanup_report


def run_cleanup(
    library: Path,
    report_directory: Path,
):

    results = analyse_library(
        library
    )


    report = generate_cleanup_report(
        results
    )


    report_directory.mkdir(
        parents=True,
        exist_ok=True,
    )


    report_file = (
        report_directory /
        "cleanup_report.txt"
    )


    report_file.write_text(
        report
    )


    return report

