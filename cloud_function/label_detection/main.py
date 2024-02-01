import functions_framework
from google.cloud import vision


def run_quickstart(file, bucket) -> vision.EntityAnnotation:

    print(file)
    print(bucket)
    # # Instantiates a client
    client = vision.ImageAnnotatorClient()

    file_uri = (f"gs://{bucket}/{file}")
    print(file_uri)
  
    image = vision.Image()
    image.source.image_uri = file_uri

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print("Labels:")
    for label in labels:
        print(label.description)

    return labels

@functions_framework.cloud_event
def hello_gcs(cloud_event):
    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    bucket = data["bucket"]
    name = data["name"]
    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]

    print(f"Event ID: {event_id}")
    print(f"Event type: {event_type}")
    print(f"Bucket: {bucket}")
    print(f"File: {name}")
    print(f"Metageneration: {metageneration}")
    print(f"Created: {timeCreated}")
    print(f"File was updated: {name}")

    run_quickstart(name, bucket)
