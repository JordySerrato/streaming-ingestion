import csv

class IngestionService:

    def process_data(
        self,
        adapter,
        query,
        chunk_size,
        output_file
    ):

        with open(
            output_file,
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

            for rows in adapter.fetch_data(
                query,
                chunk_size
            ):

                writer.writerows(rows)

                print(
                    f"Chunk procesado: {len(rows)} registros"
                )

        print("Exportación completada")