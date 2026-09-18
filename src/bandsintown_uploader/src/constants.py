import os

from dotenv import load_dotenv

load_dotenv()

INPUT_DIR = "data/"
EVENTS_KEY = "events"
JSON_EXTENSION = ".json"

GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID", "ai-technologies-ur2")
BQ_DATASET_NAME = os.getenv("BQ_DATASET_NAME", "dataset_teacher")
SA_KEY_JSON_PATH = os.getenv("SA_KEY_JSON", "secrets/sa-key-json.json")

EVENT_ATTRIBUTE_MAPPING_DICT = {
    "city": "city",
    "artistImageSrc": "artist_image_src",
    "properlySizedImageURL": "properly_sized_image_url",
    "callToActionRedirectUrl": "call_to_action_redirect_url",
    "fallbackImageUrl": "fallback_image_url",
    "artistName": "artist_name",
    "venueName": "venue_name",
    "streamingEvent": "streaming_event",
    "title": "title",
    "locationText": "location_text",
    "pinIconSrc": "pin_icon_src",
    "eventUrl": "event_url",
    "artistUrl": "artist_url",
    "watchLiveText": "watch_live_text",
    "isPlus": "is_plus",
    "callToActionText": "call_to_action_text",
    "rsvpCount": "rsvp_count",
    "rsvpCountInt": "rsvp_count_int",
    "startsAt": "starts_at",
    "endsAt": "ends_at",  # Optional field
    "timezone": "timezone",
    "displayRule": "display_rule",
    "locale": "locale",
}
