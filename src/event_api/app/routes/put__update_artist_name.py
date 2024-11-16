from fastapi import APIRouter, HTTPException, Path, Query
from google.cloud import bigquery

from ..db._config import DB_TABLE
from ..db.fetch_events import execute_query_against_db
from .security import check_token

router = APIRouter()


@router.put("/events/{event_id}/update-artist", tags=["Events"])
async def update_event_artist(
    token: str,
    event_id: str = Path(..., description="The unique ID of the event"),
    artist_name: str = Query(..., description="The new name of the artist"),
):
    """
    Endpoint to update the artist name for a specific event.
    """
    check_token(token)
    try:
        # SQL Query to update the artist name
        query = f"""
        UPDATE `{DB_TABLE}`
        SET artist_name = @artist_name
        WHERE event_id = @event_id
        """

        # Query parameters for secure execution
        query_params = [
            bigquery.ScalarQueryParameter("artist_name", "STRING", artist_name),
            bigquery.ScalarQueryParameter("event_id", "STRING", event_id),
        ]

        execute_query_against_db(
            query=query, query_params=query_params, return_df=False
        )

    except RuntimeError as e:
        raise HTTPException(
            status_code=500, detail=f"Error updating artist name: {str(e)}"
        )
