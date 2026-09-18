# data-engineering-course

Data engineering course project for the Master Data Science in Rennes.

The project scrapes events from Bandsintown, uploads them to BigQuery, and
exposes them through a small FastAPI service:

- **Scraper** (`src/bandsintown_scraper`): fetches events for a city and date
  range from Bandsintown and stores the raw pages in GCS.
- **Uploader** (`src/bandsintown_uploader`): reads the scraped events, transforms
  them, and loads them into BigQuery.
- **API** (`src/event_api`): FastAPI app to query and search the uploaded events.

## Setup

Dependencies are managed with [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

Copy `.env.example` to `.env` and fill in the values (GCP project, BigQuery
dataset/table, service account key path, API token, ...):

```bash
cp .env.example .env
```

## Running

Commands are available both as `uv run ...` and as `make` targets (the
`Makefile` automatically loads variables from `.env`).

### Scraper

```bash
uv run scrap_entry_point.py --city Paris --start-date 2026-10-01 --end-date 2026-10-31
# or
make scrape ARGS="--city Paris --start-date 2026-10-01 --end-date 2026-10-31"
```

`--city`, `--start-date`, and `--end-date` are all optional: by default the
city is Paris, the start date is today, and the end date is the end of the
current month.

### Uploader

```bash
uv run upload_entry_point.py
# or
make upload
```

### API

```bash
uv run fastapi dev src/event_api/app/main.py
# or
make api
```
