"""Models for Bird-related data."""
from typing import List, Optional
from pydantic import BaseModel

from bird_stack.db.models.base import Document

class BirdData(BaseModel):
    """Specific structure for the `data` field in the `Document` model."""
    name: str
    region: Optional[str]
    countries: List[str]
    appearances: List[str]
    other_names: Optional[List[str]]
    similar_entities: Optional[List[str]]

class BirdsResponse(BaseModel):
    """Response model for the birds endpoint."""
    birds: List[Document]
