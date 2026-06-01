import pandas as pd

from src.database.mysql_manager import (
    MySQLManager
)


class CompanyRepository:

    def get_all_data(
        self
    ):

        connection = (
            MySQLManager
            .get_connection()
        )

        query = """
        SELECT *
        FROM companies
        """

        df = pd.read_sql(
            query,
            connection
        )

        connection.close()

        return df