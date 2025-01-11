"""Models for Bird-related data."""
from typing import List, Optional, Dict, Any, TypeAlias
from pydantic import BaseModel

from bird_stack.db.models.base import Document, ExtendedQuerySuccess

class BirdData(BaseModel):
    """Specific structure for the `data` field in the `Document` model."""
    name: str
    image: str
    region: Optional[str]
    countries: List[str]
    appearances: List[str]
    other_names: Optional[List[str]]
    similar_entities: Optional[List[str]]

class BirdsResponse(BaseModel):
    """Response model for the birds endpoint."""
    birds: List[Dict[str, Any]]  # Type the birds field as a list of dictionaries

class BirdList(List[Document]):
    """Custom list class for Bird documents."""

    def	__init__(self, data: List[Document]):
        super().__init__(data)

    def get_names(self) -> List[str]:
        """Get the names of all birds in the list."""
        return [bird.data.name for bird in self]

    def filter_by_name(self, name: str) -> 'BirdList':
        """Filter the list by bird name."""
        return BirdList([bird for bird in self if bird.data.name == name])

# Define type aliases
BirdQueryResult: TypeAlias = ExtendedQuerySuccess[BirdList]
