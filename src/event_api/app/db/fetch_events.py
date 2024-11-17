import os
from typing import List, Optional, Union

import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

from ..settings import settings


def execute_query_against_db(
    query: str,
    query_params: Optional[List[bigquery.ScalarQueryParameter]] = None,
    return_df: bool = True,
) -> Optional[pd.DataFrame]:
    """
    Execute a query on BigQuery and optionally return the result as a DataFrame.

    Args:
        query (str): SQL query to execute.
        query_params (Optional[List[bigquery.ScalarQueryParameter]]): Optional query parameters for secure SQL execution.
        return_df (bool): Flag to determine if the result should be returned as a DataFrame. Defaults to True.

    Returns:
        Optional[pd.DataFrame]: The result of the query as a DataFrame if `return_df` is True, otherwise None.

    Raises:
        RuntimeError: If query execution fails.
    """

    service_account_fp = settings.service_account_fp

    if not service_account_fp:
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

    if return_df:
        return result.to_dataframe()
    return None
