import typer

from pathlib import Path

from app.importer.pipeline import import_media


cli = typer.Typer(
    name="media-organiser",
    help="A local media organisation system.",
)


@cli.command()
def import_files():
    """
    Import photos and videos.
    """

    inbox = Path("data/inbox")
    library = Path("data/library")

    results = import_media(
        inbox,
        library,
    )

    typer.echo(
        f"Imported {len(results)} files."
    )


@cli.command()
def scan():
    """
    Scan inbox for media files.
    """

    typer.echo(
        "Scanner command coming soon."
    )


def main():
    cli()


if __name__ == "__main__":
    main()

