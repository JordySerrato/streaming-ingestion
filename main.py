import pymysql
import csv

conexion = pymysql.connect(
    host="host.docker.internal",
    user="root",
    password="123456",
    database="streaming_lab"
)


cursor = conexion.cursor()



query = "SELECT * FROM clientes"

cursor.execute(query)


with open("output_stream.csv", "w", newline="", encoding="utf-8") as archivo:

    writer = csv.writer(archivo)

    # encabezados
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