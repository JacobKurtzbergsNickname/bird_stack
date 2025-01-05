"""Wrapper class for querying the database for bird data."""
from fauna import fql
from bird_stack.db.models import BirdList, BirdQueryResult
from bird_stack.db.models.utils import transform_bird_data
from bird_stack.db.fauna_client.fauna_client import fql_query

class BirdQueryWrapper:
    """That's the actual thing here"""
    def __init__(self, query_string: str):
        self.query_string = query_string
        self.raw_result: BirdQueryResult | None = None

    def wrapped_query(self) -> 'BirdQueryWrapper':
        """Execute the query and store the raw result."""
        self.raw_result = fql_query(fql(self.query_string))
        return self

    def query(self) -> 'BirdQueryWrapper':
        """Execute the query and store the raw result."""
        self.raw_result = fql_query(self.query_string)
        return self

    def transform(self) -> BirdList:
        """Transform the raw result into Document objects."""
        return transform_bird_data(self.raw_result).data