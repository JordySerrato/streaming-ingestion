import pymysql
import random
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

ciudades = [
    "Lima",
    "Bogota",
    "Santiago",
    "Quito",
    "Buenos Aires"
]

TOTAL_REGISTROS = 3000000
BATCH_SIZE = 10000

sql = """
INSERT INTO clientes(
    nombre,
    correo,
    ciudad
)
VALUES(%s,%s,%s)
"""

for inicio in range(0, TOTAL_REGISTROS, BATCH_SIZE):

    datos = []

    for i in range(inicio, inicio + BATCH_SIZE):

        nombre = f"Usuario_{i}"

        correo = f"usuario{i}@gmail.com"

        ciudad = random.choice(ciudades)

        datos.append((
            nombre,
            correo,
            ciudad
        ))

    cursor.executemany(sql, datos)

    conexion.commit()

    print(f"{inicio + BATCH_SIZE} registros insertados")

cursor.close()
conexion.close()

print("Carga masiva completada")