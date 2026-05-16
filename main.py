import pymysql
import csv
import os

from dotenv import load_dotenv

load_dotenv()

conexion = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conexion.cursor()

query = "SELECT * FROM clientes"

cursor.execute(query)

with open(
    "output_stream.csv",
    "w",
    newline="",
    encoding="utf-8"
) as archivo:

    writer = csv.writer(archivo)

    writer.writerow([
        "id",
        "nombre",
        "correo",
        "ciudad"
    ])

    while True:

        rows = cursor.fetchmany(1000)

        if not rows:
            break

        writer.writerows(rows)

        print(f"Chunk procesado: {len(rows)} registros")

cursor.close()
conexion.close()

print("Exportación completada")