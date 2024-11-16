from .get__all_events import router as get_all_events_router
from .get__search_events import router as get_search_events_router

all_routes = [get_all_events_router, get_search_events_router]
