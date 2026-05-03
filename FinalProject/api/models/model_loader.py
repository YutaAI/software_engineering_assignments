from sqlalchemy.exc import SQLAlchemyError
from ..dependencies.database import engine, Base


def index():
    try:
        Base.metadata.create_all(engine)
    except SQLAlchemyError:
        return False

    return True
