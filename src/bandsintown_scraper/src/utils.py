import json
import os
from typing import Dict, List, Union

from google.cloud import storage

from .constants import GCS_RAW_DATA_BUCKET_NAME, OUTPUT_DIR
import time
import random
from geopy.geocoders import Nominatim


def save_json_to_gcs(
    data_to_persist: Dict[str, Union[str, Dict, List]],
    execution_date: str,
    filename: str,
):
    """Write data to a JSON file in a Google Cloud Storage bucket."""
    gcs_bucket_name = GCS_RAW_DATA_BUCKET_NAME.split("://")[-1]

    client = storage.Client()
    bucket = client.bucket(gcs_bucket_name)

    gcs_object_name = os.path.join(
        "raw_data", "bands_in_town", execution_date, filename
    )

    blob = bucket.blob(gcs_object_name)

    # Convert the data to JSON and encode it as bytes
    json_data = json.dumps(data_to_persist).encode("utf-8")
    blob.upload_from_string(json_data, content_type="application/json")


def save_json(data_to_persist: Dict[str, Union[str, Dict, List]], filename: str):
    """Write data to a JSON file."""
    os.makedirs(os.path.dirname(os.path.join(OUTPUT_DIR, filename)), exist_ok=True)
    file_path = os.path.join(OUTPUT_DIR, filename)

    with open(file_path, "w") as json_file:
        json.dump(data_to_persist, json_file, indent=4)


def random_sleep(min_sleep=1, max_sleep=3):
    sleep_time = random.uniform(min_sleep, max_sleep)
    time.sleep(sleep_time)


def get_city_coordinates(city: str) -> Dict[str, float]:
    geolocator = Nominatim(user_agent="ur2-technologies")
    location = geolocator.geocode(city)

    if location:
        return {"latitude": location.latitude, "longitude": location.longitude}
    else:
        raise ValueError(f"Could not find coordinates for city: {city}")
