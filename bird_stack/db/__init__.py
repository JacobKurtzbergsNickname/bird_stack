"""This module initializes the db package."""

from .fauna_client import fauna_client, fql_query
from .models import Module, BirdData, Document
from .queries import get_birds

__all__ = [
    # FaunaDB implementation
    "fauna_client", 
    "fql_query",

    # Pydantic models
    "Module",
    "BirdData",
    "Document",

    # Query functions
    "get_birds"
]
