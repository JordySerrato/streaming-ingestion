from storage.gcs_storage import GCSStorage
from adapters.api_adapter import APIAdapter
from services.ingestion_service import IngestionService

adapter = APIAdapter()
service = IngestionService()
storage = GCSStorage()

url = "https://jsonplaceholder.typicode.com/users"

service.process_data(
    adapter=adapter,
    query=url,
    chunk_size=2,
    output_file="api_output.csv"
)
storage.upload_file(
    bucket_name="bronze-layer",
    source_file="api_output.csv",
    destination_blob="api/api_output.csv"
)