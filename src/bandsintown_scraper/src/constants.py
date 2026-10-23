import os

from dotenv import load_dotenv

load_dotenv()

# Return always the first page when using params= instead of plain url
# So we using the plain url with parameters inside it
API_URL = (
    "https://www.bandsintown.com/fr/choose-dates/fetch-next/upcomingEvents?"
    "date={start_date}T00%3A00%3A00%2C2025-01-01T23%3A00%3A00"
    "&page={page_idx}"
    "&longitude=2.3488&latitude=48.85341"
    "&genre_query=all-genres"
)
COMMON_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}

GCS_RAW_DATA_BUCKET_NAME = os.getenv(
    "GCS_RAW_DATA_BUCKET_NAME", "gs://bandsintown-raw-data"
)
OUTPUT_DIR = "data/"

# Chrome fetch() headers. Tested 2026-10-13, residential IP, 3 tries per combination.
API_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",  # needed (403 without) but not enough alone
    "Accept": "application/json, text/plain, */*",  # not required on its own
    "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.8",  # not required on its own
    # "Accept-Encoding": "gzip, deflate",  # no "br": requests can't decode Brotli without the brotli package
    "Referer": "https://www.bandsintown.com/fr/choose-dates/genre/all-genres",  # UA + Referer alone failed; mixed results elsewhere
    "sec-ch-ua": '"Chromium";v="129", "Not=A?Brand";v="8"',  # must match the User-Agent version; UA + sec-ch-ua* alone passed
    # "sec-ch-ua-mobile": "?0",  # same group as sec-ch-ua
    # "sec-ch-ua-platform": '"macOS"',  # must match the User-Agent OS
    "Sec-Fetch-Dest": "empty",  # not required on its own
    # "Sec-Fetch-Mode": "cors",  # UA + this header alone passed; "navigate" also passed with the full set
    # "Sec-Fetch-Site": "same-origin",  # not required on its own
}

USER_AGENT_LIST = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
]
