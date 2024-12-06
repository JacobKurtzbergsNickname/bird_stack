# fauna_client.pyi
"""Typing stubs for the Fauna client."""
from typing import Any

class Client:
    """Typing stub for Client class."""
    def __init__(self, secret: str) -> None: ...    # pylint: disable=unused-argument
    async def query(self, query: str) -> Any: ...   # pylint: disable=unused-argument, missing-function-docstring

fauna_client: Client

def fql_query(fql: str) -> Any: ...   # pylint: disable=unused-argument, missing-function-docstring
