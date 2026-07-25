from app.duplicates.manager import (
    find_duplicate_groups,
)



def test_duplicate_groups(tmp_path):

    library = tmp_path / "library"

    library.mkdir()


    first = library / "one.jpg"

    second = library / "two.jpg"


    first.write_text(
        "same"
    )

    second.write_text(
        "same"
    )


    groups = find_duplicate_groups(
        library
    )


    assert len(groups) == 1

    assert len(groups[0]) == 2

