"""Pydantic models for the database documents."""
from datetime import datetime
from typing import Any, Dict, Optional, TypeVar, Generic, Mapping

from pydantic import BaseModel
from fauna.encoding import QuerySuccess as BaseQuerySuccess, QueryStats

T = TypeVar('T')

class Module(BaseModel):
    """Representation of Module data type from FaunaDB."""
    name: str

class Document(BaseModel, Generic[T]):
    """Representation of Document data type from FaunaDB."""
    id: str  # pylint: disable=redefined-builtin
    coll: Module
    ts: datetime
    data: T

    def dict(self, *args, **kwargs) -> Dict[str, Any]:
        """Convert the Document instance to a dictionary."""
        return super().model_dump(*args, **kwargs)

# Usage example:
# document: Document[BirdData] = Document(id="123", coll=module, ts=timestamp, data=bird_data)

class ExtendedQuerySuccess(Generic[T], BaseQuerySuccess):
    """The result of the query with generic typing."""

    @property
    def data(self) -> T:
        """The data returned by the query. This is the result of the FQL query."""
        return self._data

    @data.setter
    def data(self, value: T) -> None:
        self._data = value

    def __init__(
        self,
        data: T,
        query_tags: Optional[Mapping[str, str]] = None,
        static_type: Optional[str] = None,
        stats: Optional[QueryStats] = None,
        summary: Optional[str] = None,
        traceparent: Optional[str] = None,
        txn_ts: Optional[int] = None,
        schema_version: Optional[int] = None,
    ):
        super().__init__(
            data=data,  # Pass data to parent class
            query_tags=query_tags,
            static_type=static_type,
            stats=stats,
            summary=summary,
            traceparent=traceparent,
            txn_ts=txn_ts,
            schema_version=schema_version,
        )
        self._data = data  # Store the typed data
