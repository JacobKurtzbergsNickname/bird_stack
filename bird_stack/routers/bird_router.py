"""Router for the Bird REST API."""
from typing import Any, List, TypeAlias
from robyn import SubRouter
from bird_stack.db.models import BirdsResponse, ExtendedQuerySuccess, Document, BirdData
from bird_stack.db.queries import get_birds

# Define a type aliases
BirdQueryResult: TypeAlias = ExtendedQuerySuccess[List[Document[BirdData]]]
BirdList: TypeAlias = List[Document]

# Create a sub-router
bird_router = SubRouter(__name__, prefix="/api/birds")

@bird_router.get("/")
async def birds(request: Any) -> BirdsResponse:
    """Get all the birds."""
    print("Request:", request)
    birds_success: BirdQueryResult = get_birds("get_all_birds")
    bird_list: BirdList = birds_success.data
    return BirdsResponse(birds=bird_list)
