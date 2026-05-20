from adapters.mysql_adapter import MySQLAdapter

from adapters.api_adapter import APIAdapter


class AdapterFactory:


    @staticmethod
    def create(source_type):


        if source_type == "mysql":

            return MySQLAdapter()


        elif source_type == "api":

            return APIAdapter()


        else:

            raise ValueError(
                f"Fuente no soportada: {source_type}"
            )