from typing import Optional, Tuple

from fastapi import APIRouter, Depends, HTTPException, Query

from ..db._config import DB_TABLE
from ..db.fetch_events import fetch_event_from_query
from .pagination import paginate
from .security import check_token

router = APIRouter()


@router.get("/events/search", tags=["Events"])
@paginate(page_size=10)
async def search_events(
    token: str,
    artistName: Optional[str] = Query(
        default=None, description="Filter events by artist name"
    ),
    venueName: Optional[str] = Query(
        default=None, description="Filter events by venue name"
    ),
    date_range: Optional[Tuple[str, str]] = Query(
        default=None, description="Date range in 'YYYY-MM-DD,YYYY-MM-DD'"
    ),
    city: Optional[str] = Query(default=None, description="Filter events by city"),
):
    """
    Search for events by artist name, venue name, date range, and city.
    Filters are applied directly in the SQL query for better performance.
    """
    check_token(token)
    try:
        # Construct SQL query with filters
        conditions = []
        if artistName:
            conditions.append(f"LOWER(artist_name) LIKE LOWER('%{artistName}%')")
        if venueName:
            conditions.append(f"LOWER(venue_name) LIKE LOWER('%{venueName}%')")
        if date_range:
            try:
                start_date, end_date = map(lambda x: x.strip(), date_range.split(","))
                conditions.append(f"event_date BETWEEN '{start_date}' AND '{end_date}'")
            except ValueError:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid date_range format. Use 'YYYY-MM-DD,YYYY-MM-DD'.",
                )
        if city:
            conditions.append(f"LOWER(city) LIKE LOWER('%{city}%')")

        # Combine conditions into WHERE clause
        where_clause = " AND ".join(conditions)
        query = f"SELECT * FROM `{DB_TABLE}`"
        if where_clause:
            query += f" WHERE {where_clause}"

        # Fetch events from BigQuery
        events_df = fetch_event_from_query(query)

        # Return the filtered DataFrame (pagination handled by the decorator)
        return events_df
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=f"Error fetching events: {e}")
