"""GET all birds from the database."""
from fauna import fql
from bird_stack.db.models import BirdList
from bird_stack.db.queries.bird_query_wrapper import BirdQueryWrapper
from bird_stack.db.queries.utils import retrieve_query


def get_birds(file_name: str) -> BirdList:
    """Get all the birds from the database."""
    bird_query = retrieve_query(file_name)
    bird_query_wrapper = BirdQueryWrapper(bird_query)
    return bird_query_wrapper.wrapped_query().transform()


def get_bird_by_name(file_name: str, bird_name: str) -> BirdList:
    """Get a bird by name."""
    return get_birds(file_name).filter_by_name(bird_name)


def get_bird_by_id(bird_id: str) -> BirdList:
    """Get a bird by ID."""
    query = fql("FictionalBirds.where(value => value.id == ${bird_id}).toArray()", bird_id=bird_id)
    bird_query_wrapper = BirdQueryWrapper(query)
    return bird_query_wrapper.query().transform()