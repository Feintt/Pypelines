from typing import Tuple, Dict

from pypelines import Pipeable
import psycopg2

postgres_config = {
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": 5432,
    "database": "postgres"
}


def start_connection(config, _changeset):
    """
    Start a connection to a PostgreSQL database using the provided configuration.
    The function expects a dictionary with the following keys:
    - user
    - password
    - host
    - port
    - database

    It does not matter the order of the keys.
    :param _changeset:
    :param config: Dictionary containing the database configuration.
    :return: A tuple indicating a change with the new connection and cursor, or an error.
    """
    try:
        connection = psycopg2.connect(
            user=config["user"],
            password=config["password"],
            host=config["host"],
            port=config["port"],
            database=config["database"]
        )
        cursor = connection.cursor()
        # Use add_change method to update the changeset
        return "change", {"connection": connection, "cursor": cursor}
    except Exception as ex:
        return "error", {"db_error": ex}


result = (Pipeable(postgres_config)
          | start_connection)
