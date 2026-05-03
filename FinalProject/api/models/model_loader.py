from . import orders, order_details, recipes, sandwiches, resources

from ..dependencies.database import engine
from sqlalchemy.exc import SQLAlchemyError


def index():
    try:
        orders.Base.metadata.create_all(engine)
        order_details.Base.metadata.create_all(engine)
        recipes.Base.metadata.create_all(engine)
        sandwiches.Base.metadata.create_all(engine)
        resources.Base.metadata.create_all(engine)
    except SQLAlchemyError:
        return False

    return True
