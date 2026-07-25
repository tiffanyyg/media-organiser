from app.database.database import engine
from app.database.models import Base


def initialise_database():
    Base.metadata.create_all(
        engine
    )

