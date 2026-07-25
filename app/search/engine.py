from app.search.queries import (
    search_filename,
)



def search_media(
    query: str,
):
    """
    Main search entry point.
    """

    return search_filename(
        query
    )

