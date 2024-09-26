import os

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

USER_AGENT_LIST = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
]
