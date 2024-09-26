import os
import requests

from .utils import save_json, random_sleep, get_city_coordinates
from .scrap_one_page import scrap_one_page
import logging

logging.basicConfig(level=logging.INFO)


def scrap_multiple_pages(
    start_date: str,
    end_date: str,
    city_latitude: float,
    city_longitude: float,
    max_page: int = 30,
):
    """Scrap all events of a city from bands in town internal API"""
    logger = logging.getLogger(__name__)
    session = requests.Session()

    has_next_page = True
    page_idx = 0
    previous_page_event_url_list = []
    total_event_scrapped = 0

    while has_next_page and page_idx < max_page:
        page_idx += 1
        random_sleep()
        response_dict = scrap_one_page(
            session,
            start_date,
            end_date,
            city_latitude,
            city_longitude,
            page_idx,
        )

        current_page_event_list = response_dict.get("events")

        if len(current_page_event_list) == 0:
            return total_event_scrapped

        current_page_event_url_list = response_dict.get("events")[0]["eventUrl"]

        if response_dict.get("urlForNextPageOfEvents") is None:
            has_next_page = False

        if (
            response_dict.get("events") is None
            or current_page_event_url_list == previous_page_event_url_list
        ):
            return total_event_scrapped

        previous_page_event_url_list = current_page_event_url_list
        filename = os.path.join(start_date, f"events-page-{page_idx}.json")
        save_json(response_dict, filename)
        total_event_scrapped += len(current_page_event_url_list)
        logging.info(f"Events from page {page_idx} saved")

    return total_event_scrapped
