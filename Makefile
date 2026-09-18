-include .env
export

.PHONY: scrape upload api

scrape:
	uv run scrap_entry_point.py $(ARGS)

upload:
	uv run upload_entry_point.py

api:
	uv run fastapi dev src/event_api/app/main.py
