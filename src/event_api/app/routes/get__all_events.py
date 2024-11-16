from typing import Dict, List, Optional

from fastapi import APIRouter, HTTPException, Query
from pandas import DataFrame

from ..db._config import DB_TABLE
from ..db.fetch_events import fetch_event_from_query
from .pagination import paginate

router = APIRouter()


@router.get("/events", tags=["Events"])
@paginate(page_size=10)
async def get_all_events(
    city: Optional[str] = Query(default=None, description="Filter events by city"),
):
    """
    Endpoint to fetch all events from the BigQuery table with optional city filtering.
    """
    query = f"SELECT * FROM `{DB_TABLE}`"

    try:
        events_df = fetch_event_from_query(query)

        if city:
            events_df = events_df[events_df["city"] == city]

        return events_df
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=f"Error fetching events: {e}")
