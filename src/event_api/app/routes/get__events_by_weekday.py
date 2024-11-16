from datetime import date, timedelta

import pandas as pd
from fastapi import APIRouter, HTTPException, Query
from pandas import DataFrame

from ..db._config import DB_TABLE
from ..db.fetch_events import fetch_event_from_query
from .security import check_token

router = APIRouter()


@router.get("/events/by-day-of-week", tags=["Events"])
async def get_events_by_day_of_week(
    token: str,
    start_date: date = Query(..., description="Start date of the week (YYYY-MM-DD)"),
):
    """
    Endpoint to fetch the number of events grouped by the day of the week for the specified week.
    """
    check_token(token)
    try:
        # Calculate the end date of the week
        end_date = start_date + timedelta(days=6)

        # Query to filter events for the specified week
        query = f"""
        SELECT date(starts_at) as event_date
        FROM `{DB_TABLE}`
        WHERE date(starts_at) BETWEEN '{start_date}' AND '{end_date}'
        """

        # Fetch events
        events_df: DataFrame = fetch_event_from_query(query)

        # Check if events exist
        if events_df.empty:
            return {"message": "No events found for the specified week", "data": []}

        # Transform the date into the day of the week and count occurrences
        events_df["event_date"] = pd.to_datetime(events_df["event_date"])
        events_df["day_of_week"] = events_df["event_date"].dt.day_name()
        distribution = (
            events_df.groupby("day_of_week")
            .size()
            .reset_index(name="event_count")
            .to_dict(orient="records")
        )

        return {"start_date": start_date, "end_date": end_date, "data": distribution}

    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=f"Error fetching events: {e}")
