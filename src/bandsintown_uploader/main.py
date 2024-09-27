import pandas as pd
from .src.constants import INPUT_DIR
from .src.transform import transform_events
from .src.read import read_events
from .src.upload import upload_to_bigquery
import logging

logging.basicConfig(level=logging.INFO)


def upload_events():
    logging.info("Reading events from input directory ..")
    raw_event_list = read_events(INPUT_DIR)
    logging.info("Transforming events ..")
    transformed_event_pdf = transform_events(raw_event_list)
    upload_to_bigquery(transformed_event_pdf, "events")
    logging.info(f"{len(transformed_event_pdf.index)} events uploaded to BigQuery")

    return transformed_event_pdf
