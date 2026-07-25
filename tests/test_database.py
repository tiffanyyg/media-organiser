from app.database.init import initialise_database


def test_database_creation():
    initialise_database()

    assert True

