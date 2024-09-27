import os

import pandas as pd
from google.oauth2 import service_account
from pandas_gbq import to_gbq


def upload_to_bigquery(
    df: pd.DataFrame,
    table_name: str,
    project_id: str = "ai-technologies-ur2",
):
    """Uploads a pandas DataFrame to BigQuery using a service account.

    Args:
        df (pd.DataFrame): The DataFrame to upload.
        table_name (str): The target table in the format 'dataset.table'.
        project_id (str): The GCP project ID.
        key_path (str): Path to the service account JSON key file.
    """
    destination_table = f"dataset_teacher.{table_name}"
    credentials = service_account.Credentials.from_service_account_file(
        os.getenv("SA_KEY_JSON", "secrets/sa-key-json.json")
    )

    to_gbq(
        df,
        destination_table,
        project_id=project_id,
        if_exists="replace",
        credentials=credentials,
    )
