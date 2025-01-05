"""Utility functions for working with models."""
from datetime import datetime, timezone
from os import getenv
from dotenv import load_dotenv
from fauna.encoding import QuerySuccess
from bird_stack.db.models import Document, ExtendedQuerySuccess, Module, BirdData, BirdQueryResult, BirdList

# Dotenv
load_dotenv()
FICTIONAL_BIRD_COLLECTION = getenv("FICTIONAL_BIRD_COLLECTION", "FictionalBirds")

def transform_bird_data(raw_result: QuerySuccess) -> BirdQueryResult:
    """Transform raw FaunaDB query results into Pydantic models."""
    print("Raw result:", raw_result)  # See complete result
    print("Raw data structure:", raw_result.data)  # See data structure

    # Transform assuming bird IS the data
    transformed_data = [
        Document(
            id=str(bird.get("ref", {}).get("id", "unknown")),  # Get ID from ref
            coll=Module(name=FICTIONAL_BIRD_COLLECTION),
            ts=datetime.now(timezone.utc),
            data=BirdData(**bird)  # Use bird directly as data
        )
        for bird in raw_result.data
    ]

    list_data = BirdList(transformed_data)

    return ExtendedQuerySuccess(
        data=list_data,
        query_tags=raw_result.query_tags,
        static_type=raw_result.static_type,
        stats=raw_result.stats,
        summary=raw_result.summary,
        traceparent=raw_result.traceparent,
        txn_ts=raw_result.txn_ts,
        schema_version=raw_result.schema_version
    )


#TODO: Add a transform function for a single bird. :)
