import pandas as pd
from .src.constants import INPUT_DIR
from .src.transform import transform_events
from .src.read import read_events


def upload_events():
    raw_event_list = read_events(INPUT_DIR)
    transformed_event_pdf = transform_events(raw_event_list)
    return transformed_event_pdf
