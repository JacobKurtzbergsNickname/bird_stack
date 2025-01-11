# bird_stack/app.py
"""A simple Robyn app to display mythical birds."""
from os import getenv
from typing import Any, Dict

from robyn import ALLOW_CORS, Robyn

from dotenv import load_dotenv
from bird_stack.routers.bird_router import bird_router

load_dotenv()
PORT = getenv("PORT")

app = Robyn(__file__)
app.include_router(bird_router)
ALLOW_CORS(app, origins = ["http://localhost:5173"])


# API root, former entry point
@app.get("/api")
async def root(request: Any) -> Dict[str, str]:
    """Root route"""
    print("Request:", request)
    return {"message": "Down amongst the darkened roots..."}


def main() -> None:
    """Running the Robyn app"""
    port: int = int(PORT) if PORT else 8000
    print(f"Starting server on port {port}")
    print(f"Open http://localhost:{port} in your browser")
    app.start(port=port)


if __name__ == "__main__":
    main()
