from fastapi import FastAPI

from .routes import get_all_events_router

app = FastAPI(
    title="Events API",
    description="An API to analyse musical events and predit affluence",
    version="0.0.1",
)

app.include_router(get_all_events_router)


# Run a startup log to verify routes are loaded
@app.on_event("startup")
async def startup_event():
    print(f"Routes: {app.routes}")
