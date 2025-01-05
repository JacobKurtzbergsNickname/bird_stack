"""Router for the Bird REST API."""
from typing import Any
from robyn import SubRouter
from bird_stack.db.models import BirdsResponse, BirdList
from bird_stack.db.queries import get_birds, get_bird_by_id

# Create a sub-router
bird_router = SubRouter(__name__, prefix="/api/birds")

@bird_router.get("/")
async def birds() -> BirdsResponse:
    """Get all the birds."""
    bird_list: BirdList = get_birds("get_all_birds")
    return BirdsResponse(birds=[bird.data.dict() for bird in bird_list])


@bird_router.get("/:bird_id")
async def bird_by_id(request: Any) -> BirdsResponse:
    """Get a bird by ID."""
    bird_list: BirdList = get_bird_by_id(request.path_params["bird_id"])
    return BirdsResponse(birds=[bird.data.dict() for bird in bird_list])
