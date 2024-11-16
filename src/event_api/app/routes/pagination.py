from functools import wraps
from typing import Any, Callable, Dict

from pandas import DataFrame


def paginate(page_size: int = 10):
    """
    A decorator to handle pagination for endpoints.
    Adds metadata about total items, pages, and the current page.
    """

    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs) -> Dict[str, Any]:
            # Extract the page number from the kwargs
            page = kwargs.pop("page", 1)
            result = await func(*args, **kwargs)

            if not isinstance(result, DataFrame):
                raise ValueError(
                    "The decorated function must return a pandas DataFrame."
                )

            # Pagination logic
            start_idx = (page - 1) * page_size
            end_idx = start_idx + page_size
            paginated_df = result.iloc[start_idx:end_idx]

            return {
                "data": paginated_df.to_dict(orient="records"),
                "metadata": {
                    "total_pages": (len(result) + page_size - 1) // page_size,
                    "page": page,
                    "page_size": page_size,
                    "total_items": len(result),
                },
            }

        return wrapper

    return decorator
