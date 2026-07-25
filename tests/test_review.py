from app.cleanup.reviewer import move_to_review



def test_move_to_review(tmp_path):

    original = tmp_path / "photo.jpg"

    original.write_text(
        "test"
    )


    review_folder = (
        tmp_path /
        "review"
    )


    moved = move_to_review(
        [original],
        review_folder,
    )


    assert len(moved) == 1

    assert moved[0].exists()

    assert not original.exists()

