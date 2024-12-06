"""Visualising data from FaunaDB in Python."""
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from pydantic import BaseModel

class Module(BaseModel):
    """Representation of Module data type from FaunaDB."""
    name: str

class BirdData(BaseModel):
    """Specific structure for the `data` field in the `Document` model."""
    name: str
    region: Optional[str]
    countries: List[str]
    appearances: List[str]
    other_names: Optional[List[str]]
    similar_entities: Optional[List[str]]

class Document(BaseModel):
    """Representation of Document data type from FaunaDB."""
    id: str  # pylint: disable=redefined-builtin
    coll: Module
    ts: datetime
    data: BirdData

    def dict(self, *args, **kwargs) -> Dict[str, Any]:
        """Convert the Document instance to a dictionary."""
        return super().dict(*args, **kwargs)

# Sample query result from Fauna
query_result = [
    Document(
        id='416526284281086155',  # pylint: disable=redefined-builtin
        coll=Module(name='FictionalBirds'),
        ts=datetime(2024, 12, 6, 12, 47, 49, tzinfo=timezone.utc),
        data=BirdData(
            name='Roc',
            region='Middle East',
            countries=['Iran', 'Iraq', 'Yemen', 'China', 'Saudi-Arabia'],
            appearances=['Snakes & Ladders'],
            other_names=['Rukh'],
            similar_entities=['Garuda', 'Simurgh', 'Phoenix', 'Thunderbird'],
        ),
    )
]

# Convert to structured models
structured_docs: List[Document] = [Document(**doc.dict()) for doc in query_result]

# Print structured documents
for doc in structured_docs:
    print(doc)
