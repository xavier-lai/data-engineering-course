from functools import reduce
from .constants import EVENT_ATTRIBUTE_MAPPING_DICT, EVENTS_KEY
from typing import List, Dict, Any
import pandas as pd


def transform_events(event_raw_list: List[Dict[str, Any]]):
    all_events = []

    for raw_event_dict in event_raw_list:
        city = raw_event_dict.get("city", None)  # Extract city from the page level
        events = raw_event_dict.get(EVENTS_KEY, [])  # Extract events from the page

        normalized_events = [
            {**_normalize_event(event), "city": city} for event in events
        ]

        all_events.extend(normalized_events)

    event_pdf = pd.DataFrame(all_events)

    event_pdf["event_id"] = (
        event_pdf["event_url"].str.split("fr/e/").str[1].str.split("-").str[0]
    )

    return event_pdf


def _normalize_event(event):
    """Ensures all expected fields are present in the event dict."""
    return {
        renamed_field: event.get(field, None)
        for field, renamed_field in EVENT_ATTRIBUTE_MAPPING_DICT.items()
    }
