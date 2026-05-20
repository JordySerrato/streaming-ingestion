import pymysql

from config.settings import DB_CONFIG
from ports.base_adapter import BaseAdapter

class MySQLAdapter(BaseAdapter):
    def connect(self):

        return pymysql.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"]
        )

    def fetch_data(self, query, chunk_size):

        conexion = self.connect()

        cursor = conexion.cursor()

        cursor.execute(query)

        while True:

            rows = cursor.fetchmany(chunk_size)

            if not rows:
                break

            yield rows

        cursor.close()

        conexion.close()