from datetime import datetime, timedelta
import logging

from .src.scrap_multiple_pages import scrap_multiple_pages
from .src.utils import get_city_coordinates


logging.basicConfig(level=logging.INFO)


def extract_events(city: str, start_date: str, end_date: str, max_page: int = 30):
    """
    Main function to scrape events for each day between start_date and end_date.
    Calls scrap_multiple_pages for every single day in the date range.
    """
    logger = logging.getLogger(__name__)
    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(end_date, "%Y-%m-%d")
    total_events = 0
    logging.info(f"Get coordinates for {city} ...")
    city_coordinates = get_city_coordinates(city)

    while start_dt <= end_dt:
        current_date_str = start_dt.strftime("%Y-%m-%d")
        logger.info(f"Scraping events for {city} on {current_date_str} ...")

        # Call scrap_multiple_pages for each day
        current_day_events_scraped = scrap_multiple_pages(
            current_date_str,
            current_date_str,
            city,
            city_coordinates["latitude"],
            city_coordinates["longitude"],
            max_page,
        )
        total_events += current_day_events_scraped

        logger.info(
            f"Total events scraped for {current_date_str}: {current_day_events_scraped}"
        )

        start_dt += timedelta(days=1)

    logger.info(f"Finished scraping events for {city} from {start_date} to {end_date}.")
    logger.info(f"Total events scraped: {total_events}")
