import mysql.connector

from src.config.settings import (
    settings
)

from src.core.logger import (
    logger
)


class MySQLManager:

    @staticmethod
    def get_connection():

        try:

            connection = (
                mysql.connector.connect(

                    host=
                    settings
                    .MYSQL_HOST,

                    port=
                    settings
                    .MYSQL_PORT,

                    user=
                    settings
                    .MYSQL_USER,

                    password=
                    settings
                    .MYSQL_PASSWORD,

                    database=
                    settings
                    .MYSQL_DATABASE
                )
            )

            logger.info(
                "MySQL connected"
            )

            return connection

        except Exception as e:

            logger.error(
                str(e)
            )

            raise Exception(
                "MySQL connection failed"
            )