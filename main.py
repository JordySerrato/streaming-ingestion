import json

from datetime import datetime

from services.ingestion_service import IngestionService

from factories.adapter_factory import AdapterFactory

from config.settings import (
    TABLE_NAME,
    CHUNK_SIZE,
    OUTPUT_FILE,
    SOURCE_TYPE
)


adapter = AdapterFactory.create(
    SOURCE_TYPE
)


service = IngestionService()


with open(
    "manifest.json",
    "r"
) as file:

    manifest = json.load(file)


ultima_fecha = manifest[
    "last_updated_at"
]


if SOURCE_TYPE == "mysql":

    query = f"""
    SELECT *
    FROM {TABLE_NAME}
    WHERE updated_at > '{ultima_fecha}'
    """


elif SOURCE_TYPE == "api":

    query = "https://jsonplaceholder.typicode.com/users"


elif SOURCE_TYPE == "mongo":

    query = None


service.process_data(
    adapter=adapter,
    query=query,
    chunk_size=CHUNK_SIZE,
    output_file=OUTPUT_FILE
)


nuevo_manifest = {
    "last_updated_at": str(
        datetime.now()
    )
}


with open(
    "manifest.json",
    "w"
) as file:

    json.dump(
        nuevo_manifest,
        file,
        indent=4
    )


print(
    "Manifest actualizado"
)