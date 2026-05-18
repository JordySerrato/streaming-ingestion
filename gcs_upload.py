from google.cloud import storage
import os

os.environ["STORAGE_EMULATOR_HOST"] = "http://localhost:4443"

client = storage.Client(project="test-project")

bucket_name = "bronze-layer"

try:
    bucket = client.get_bucket(bucket_name)

except:
    bucket = client.create_bucket(bucket_name)

blob = bucket.blob("output_stream.csv")

blob.upload_from_filename("output_stream.csv")

print("Archivo subido al bucket Bronze")