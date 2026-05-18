import os

from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

TABLE_NAME = os.getenv("TABLE_NAME")

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE"))

OUTPUT_FILE = os.getenv("OUTPUT_FILE")