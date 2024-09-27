from src.bandsintown_uploader.main import upload_events

event_pdf = upload_events()
event_pdf.to_csv("event_pdf.csv", index=False)
