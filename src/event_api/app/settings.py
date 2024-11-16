from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    gcp_project_id: str = Field(alias="gcp_project_id")
    bq_dataset_name: str = Field(alias="bq_dataset_name")
    bq_table_name: str = Field(alias="bq_table_name")
    service_account_fp: str

    class Config:
        env_file = ".env"
        populate_by_name = True  # Allow using field names in code


settings = Settings()
