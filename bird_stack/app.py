"""A simple example of a Robyn app."""
from os     import getenv
from typing import Any, Dict, List
from robyn  import Robyn
from dotenv import load_dotenv

from bird_stack.db.models   import Document, ExtendedQuerySuccess
from bird_stack.db.models.bird_data import BirdData, BirdsResponse
from bird_stack.db.queries  import get_birds

load_dotenv()
PORT = getenv("PORT")

app = Robyn(__file__)

@app.get("/")
async def root(request: Any) -> Dict[str, str]:
    """Root route"""
    print("Request:", request)
    return {"message": "Down amongst the darkened roots..."}

@app.get("/birds")
async def birds(request: Any) -> BirdsResponse:
    """Get all the birds."""
    print("Request:", request)
    birds_success: ExtendedQuerySuccess[List[Document[BirdData]]] = get_birds("get_all_birds")
    bird_list: List[Document] = birds_success.data
    return BirdsResponse(birds=bird_list)

def main() -> None:
    """Running the Robyn app"""
    port: int = int(PORT) if PORT else 8000
    print(f"Starting server on port {port}")
    print(f"Open http://localhost:{port}")

    app.start(port=port)



if __name__ == "__main__":
    main()
