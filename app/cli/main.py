import typer

from pathlib import Path

from app.importer.pipeline import import_media
from app.cleanup.service import run_cleanup


cli = typer.Typer(
    name="media-organiser",
    help="A local media organisation system.",
    invoke_without_command=False,
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
    Analyse library for cleanup candidates.
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


def main():

    cli()


if __name__ == "__main__":

    main()

