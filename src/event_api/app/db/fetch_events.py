import os
from typing import List, Optional

import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

from ..settings import settings


def fetch_event_from_query(
    query: str,
    query_params: Optional[List[bigquery.ScalarQueryParameter]] = None,
) -> pd.DataFrame:
    """
    Fetch events from BigQuery based on a provided SQL query.

    Args:
        query (str): SQL query to execute.
        query_params (Optional[List[bigquery.ScalarQueryParameter]]): Optional query parameters for secure SQL execution.

    Returns:
        Events fetched from BigQuery as a pandas DataFrame.
    """

    service_account_fp = settings.service_account_fp

    if service_account_fp is None:
        raise ValueError("SERVICE_ACCOUNT_FP environment variable must be set")

    credentials = service_account.Credentials.from_service_account_file(
        service_account_fp
    )
    client = bigquery.Client(credentials=credentials)

    job_config = bigquery.QueryJobConfig(query_parameters=query_params or [])

    try:
        query_job = client.query(query, job_config=job_config)
        result = query_job.result()
    except Exception as e:
        raise RuntimeError(f"Failed to execute query: {str(e)}")

    df = result.to_dataframe()
    return df
