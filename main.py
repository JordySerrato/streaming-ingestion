from adapters.mysql_adapter import MySQLAdapter

from services.ingestion_service import IngestionService

from config.settings import (
    TABLE_NAME,
    CHUNK_SIZE,
    OUTPUT_FILE
)

adapter = MySQLAdapter()

service = IngestionService()

query = f"SELECT * FROM {TABLE_NAME}"

service.process_data(
    adapter=adapter,
    query=query,
    chunk_size=CHUNK_SIZE,
    output_file=OUTPUT_FILE
)