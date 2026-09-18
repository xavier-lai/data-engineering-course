import argparse
import calendar
from datetime import date

from src.bandsintown_scraper import extract_events

DATE_FORMAT = "%Y-%m-%d"


def _end_of_month(today: date) -> str:
    last_day = calendar.monthrange(today.year, today.month)[1]
    return today.replace(day=last_day).strftime(DATE_FORMAT)


def _parse_args() -> argparse.Namespace:
    today = date.today()
    parser = argparse.ArgumentParser(
        description="Scrape Bandsintown events for a city."
    )
    parser.add_argument(
        "--city", default="Paris", help="City to scrape events for (default: Paris)"
    )
    parser.add_argument(
        "--start-date",
        default=today.strftime(DATE_FORMAT),
        help="Start date in YYYY-MM-DD format (default: today)",
    )
    parser.add_argument(
        "--end-date",
        default=_end_of_month(today),
        help="End date in YYYY-MM-DD format (default: end of current month)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    extract_events(args.city, args.start_date, args.end_date)
