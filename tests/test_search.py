from pathlib import Path

from app.search.engine import search_media



def test_search_empty_database():

    results = search_media(
        "nothing"
    )

    assert isinstance(
        results,
        list,
    )

