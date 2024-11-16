import os

from ..settings import settings

GCP_PROJECT_ID = settings.gcp_project_id
BQ_DATASET_NAME = settings.bq_dataset_name
BQ_TABLE_NAME = settings.bq_table_name

DB_TABLE = f"{GCP_PROJECT_ID}.{BQ_DATASET_NAME}.{BQ_TABLE_NAME}"
