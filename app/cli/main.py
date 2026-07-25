from pathlib import Path

import typer

from app.importer.pipeline import import_media

from app.cleanup.service import (
    run_cleanup,
)

from app.cleanup.review_service import (
    run_review,
)

from app.duplicates.service import (
    run_duplicate_review,
)


cli = typer.Typer(
    name="media-organiser",
    help="A local media organisation system.",
)



@cli.command(
    name="import-files"
)
def import_files():

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

    from app.importer.scanner import scan_directory


    files = scan_directory(
        Path("data/inbox")
    )


    typer.echo(
        f"Found {len(files)} files."
    )



@cli.command()
def cleanup():

    report = run_cleanup(
        Path("storage/library"),
        Path("storage/reports"),
    )


    typer.echo(
        report
    )



@cli.command()
def review():

    results = run_review(
        Path("storage/library"),
        Path("storage/review"),
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



@cli.command()
def duplicates():

    results = run_duplicate_review(
        Path("storage/library"),
        Path("storage/review/duplicates"),
        Path("storage/reports"),
    )


    typer.echo(
        "DUPLICATE REVIEW COMPLETE"
    )


    typer.echo(
        f"Groups found: {len(results['groups'])}"
    )


    typer.echo(
        f"Files moved: {len(results['moved'])}"
    )



def main():

    cli()



if __name__ == "__main__":
    main()

