from fastapi import FastAPI

from .routes import all_routes

app = FastAPI(
    title="Events API",
    description="An API to analyse musical events and predit affluence",
    version="0.0.1",
)


for route in all_routes:
    app.include_router(route)
