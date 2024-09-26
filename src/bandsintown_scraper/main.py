import requests


from .src.exceptions import ScrapingException

from .src.utils import save_json, random_sleep, get_city_coordinates
from .src.scrap_one_page import scrap_one_page
import logging

logging.basicConfig(level=logging.INFO)


def extract_events(city: str, start_date: str, end_date: str):
    """Scrap all events of a city from bands in town internal API"""
    logger = logging.getLogger(__name__)
    session = requests.Session()

    logger.info(f"Scraping events for {city} from {start_date} to {end_date} ...")
    has_next_page = True
    page_idx = 0
    logging.info(f"Get coordinates for {city} ...")
    city_coordinates = get_city_coordinates(city)
    previous_page_event_url_list = []
    while has_next_page:
        page_idx += 1
        random_sleep()
        response_dict = scrap_one_page(
            session,
            start_date,
            end_date,
            city_coordinates["latitude"],
            city_coordinates["longitude"],
            page_idx,
        )
        current_page_event_url_list = response_dict.get("events")[0]["eventUrl"]

        if response_dict.get("urlForNextPageOfEvents") is None:
            has_next_page = False

        if (
            response_dict.get("events") is None
            or current_page_event_url_list == previous_page_event_url_list
        ):
            logging.info(f"No more events found for {city}")
            return

        previous_page_event_url_list = current_page_event_url_list
        filename = f"events-{city}-page-{page_idx}.json"
        save_json(response_dict, filename)
        logging.info(f"Events from page {page_idx} saved")

    logging.info(f"{page_idx} pages have been scraped sucessfully")
