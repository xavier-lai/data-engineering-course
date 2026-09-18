import pandas as pd
from google.oauth2 import service_account
from pandas_gbq import to_gbq

from .constants import BQ_DATASET_NAME, GCP_PROJECT_ID, SA_KEY_JSON_PATH


def upload_to_bigquery(
    df: pd.DataFrame,
    table_name: str,
    project_id: str = GCP_PROJECT_ID,
):
    """Uploads a pandas DataFrame to BigQuery using a service account.

    Args:
        df (pd.DataFrame): The DataFrame to upload.
        table_name (str): The target table in the format 'dataset.table'.
        project_id (str): The GCP project ID.
        key_path (str): Path to the service account JSON key file.
    """
    destination_table = f"{BQ_DATASET_NAME}.{table_name}"
    credentials = service_account.Credentials.from_service_account_file(
        SA_KEY_JSON_PATH
    )

    to_gbq(
        df,
        destination_table,
        project_id=project_id,
        if_exists="replace",
        credentials=credentials,
    )
