from pathlib import Path

import typer

from app.importer.pipeline import import_media
from app.cleanup.service import run_cleanup
from app.cleanup.review_service import run_review


cli = typer.Typer(
    name="media-organiser",
    help="A local media organisation system.",
)


@cli.command(
    name="import-files"
)
def import_files():

    """
    Import photos and videos.
    """

    inbox = Path(
        "data/inbox"
    )

    library = Path(
        "storage/library"
    )


    report = import_media(
        inbox,
        library,
    )


    typer.echo(
        report.summary()
    )



@cli.command()
def scan():

    """
    Scan inbox for media files.
    """

    from app.importer.scanner import scan_directory


    inbox = Path(
        "data/inbox"
    )


    files = scan_directory(
        inbox
    )


    typer.echo(
        f"Found {len(files)} files."
    )



@cli.command()
def cleanup():

    """
    Analyse library and create cleanup report.
    """

    library = Path(
        "storage/library"
    )

    reports = Path(
        "storage/reports"
    )


    report = run_cleanup(
        library,
        reports,
    )


    typer.echo(
        report
    )



@cli.command()
def review():

    """
    Move cleanup candidates into review folders.
    """

    library = Path(
        "storage/library"
    )

    review_folder = Path(
        "storage/review"
    )


    results = run_review(
        library,
        review_folder,
    )


    typer.echo(
        "REVIEW COMPLETE"
    )

    typer.echo(
        f"Screenshots moved: {len(results['screenshots'])}"
    )

    typer.echo(
        f"Large files moved: {len(results['large_files'])}"
    )



def main():

    cli()



if __name__ == "__main__":
    main()

