import os

from google.cloud import storage

os.environ["STORAGE_EMULATOR_HOST"] = "http://localhost:4443"

class GCSStorage:

    def upload_file(
        self,
        bucket_name,
        source_file,
        destination_blob
    ):

        client = storage.Client(
            project="test-project"
        )

        try:

            bucket = client.get_bucket(
                bucket_name
            )

        except Exception:

            bucket = client.create_bucket(
                bucket_name
            )

        blob = bucket.blob(
            destination_blob
        )

        blob.upload_from_filename(
            source_file
        )

        print(
            f"{source_file} subido a {bucket_name}"
        )