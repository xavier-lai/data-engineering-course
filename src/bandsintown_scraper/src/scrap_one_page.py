from json import JSONDecodeError
from typing import Any, Dict

import requests

from .constants import API_URL, USER_AGENT_LIST
from .exceptions import ScrapingException
import random
from typing import Dict, Any
from .utils import get_city_coordinates


def scrap_one_page(
    session: requests.Session,
    start_date: str,
    end_date: str,
    city_latitude: float,
    city_longitude: float,
    page_idx: int,
) -> Dict[str, Any]:
    header_dict = _get_header_dict()
    param_dict = _get_params_dict(
        page_idx, start_date, end_date, city_latitude, city_longitude
    )
    response = session.get(
        "https://www.bandsintown.com/fr/choose-dates/fetch-next/upcomingEvents",
        headers=header_dict,
        params=param_dict,
    )
    try:
        response_dict = response.json()
        return response_dict
    except JSONDecodeError as error:
        raise ScrapingException(
            f"Error fetching data : response {response.status_code}"
        ) from error


def _get_header_dict() -> Dict[str, str]:
    return {"User-Agent": random.choice(USER_AGENT_LIST)}


def _get_params_dict(
    page_idx: int,
    start_date: str,
    end_date: str,
    city_latitude: float,
    city_longitude: float,
) -> Dict[str, Any]:
    return {
        "page": page_idx,
        "date": f"{start_date}T00:00:00,{end_date}T23:00:00",
        "latitude": city_latitude,
        "longitude": city_longitude,
        "genre_query": "all-genres",
    }
