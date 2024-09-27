import os
import json
from .constants import JSON_EXTENSION


def read_events(directory: str) -> list:
    """Reads all JSON files in the directory."""
    persisted_json_list = _list_json_files(directory)
    return [_load_json(file_path) for file_path in persisted_json_list]


def _list_json_files(directory: str) -> list:
    """Lists all JSON files in the directory."""
    return [
        os.path.join(dirpath, filename)
        for dirpath, _, filenames in os.walk(directory)
        for filename in filenames
        if filename.endswith(JSON_EXTENSION)
    ]


def _load_json(file_path: str) -> dict:
    """Loads JSON data from a given file."""
    with open(file_path, "r", encoding="utf-8") as f:
        raw_event_dict = json.load(f)
    city = file_path.split("/")[1]
    raw_event_dict["city"] = city.lower()
    return raw_event_dict
