import pymysql
import csv

# =========================================
# CONEXION MYSQL
# =========================================

conexion = pymysql.connect(
    host="host.docker.internal",
    user="root",
    password="123456",
    database="streaming_lab"
)

# =========================================
# CURSOR
# =========================================

cursor = conexion.cursor()

# =========================================
# QUERY
# =========================================

query = "SELECT * FROM clientes"

cursor.execute(query)

# =========================================
# CREAR CSV
# =========================================

with open("output_stream.csv", "w", newline="", encoding="utf-8") as archivo:

    writer = csv.writer(archivo)

    # encabezados
    writer.writerow([
        "id",
        "nombre",
        "correo",
        "ciudad"
    ])

    # =====================================
    # STREAMING POR CHUNKS
    # =====================================

    while True:

        rows = cursor.fetchmany(1000)

        if not rows:
            break

        writer.writerows(rows)

        print(f"Chunk procesado: {len(rows)} registros")

# =========================================
# CERRAR
# =========================================

cursor.close()
conexion.close()

print("Exportación completada")