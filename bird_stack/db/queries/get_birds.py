"""GET all birds from the database."""
from typing import List
from fauna import fql
from bird_stack.db.models import Document, ExtendedQuerySuccess
from bird_stack.db import fql_query
from bird_stack.db.models.utils import transform_bird_data
from bird_stack.db.queries.utils import retrieve_query

def get_birds(file_name: str) -> ExtendedQuerySuccess[List[Document]]:
    """Get all the birds from the database."""
    query_string = retrieve_query(file_name)

    # Transform the raw data into Document objects first
    raw_result = fql_query(fql(query_string))
    return transform_bird_data(raw_result)
