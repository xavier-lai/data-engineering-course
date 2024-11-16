from .get__all_events import router as get_all_events_router
from .get__events_by_weekday import router as get_events_by_weekday_router
from .get__search_events import router as get_search_events_router
from .put__update_artist_name import router as put__update_artist_name_router

all_routes = [
    get_all_events_router,
    get_search_events_router,
    get_events_by_weekday_router,
    put__update_artist_name_router,
]
