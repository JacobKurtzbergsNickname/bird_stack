"""Initialize the Fauna client to connect to the database."""
from os import getenv
from typing import Any
from dotenv import load_dotenv
from fauna.client import Client

load_dotenv()
BIRD_KING = getenv("BIRD_KING")

# Initialize the client to connect to Fauna
fauna_client = Client(secret=BIRD_KING)

def fql_query(fql: str) -> Any:
    """Query the database."""
    return fauna_client.query(fql)
