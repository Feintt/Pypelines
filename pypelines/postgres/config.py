import psycopg2


def start_connection(config):
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
        match config:
            case {"user": user, "password": password, "host": host, "port": port, "database": database}:
                connection = psycopg2.connect(
                    user=user,
                    password=password,
                    host=host,
                    port=port,
                    database=database
                )
                cursor = connection.cursor()
                # Use add_change method to update the changeset
                return "change", {"connection": connection, "cursor": cursor}
            case _:
                raise ValueError(
                    "Invalid configuration for PostgreSQL connection, please provide user, password, host, port and database.")

    except Exception as ex:
        raise ex


def execute_query(_data, query, args=None, changeset=None):
    """
    Execute a query in the database.
    :param _config:
    :param query: The SQL query to execute.
    :param args: The arguments for the SQL query.
    :param changeset: The changeset containing the database connection and cursor.
    :return: The changeset, potentially with modifications based on the query execution.
    """
    try:
        cursor = changeset["changes"].get("cursor")
        if args:
            cursor.execute(query, args)
        else:
            cursor.execute(query)
        changeset["changes"]["connection"].commit()
        return "change", {}
    except Exception as ex:
        return "error", {"db_error": str(ex)}


def fetch_query(_data, query, args=None, changeset=None):
    """
    Fetch the results of a query.
    :param _config:
    :param query: The SQL query to fetch results for.
    :param args: The arguments for the SQL query.
    :param changeset: The changeset containing the database connection and cursor.
    :return: The query results or an error.
    """
    try:
        cursor = changeset["changes"].get("cursor")
        if args:
            cursor.execute(query, args)
        else:
            cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Exception as ex:
        return "error", {"db_error": str(ex)}


def get_all(_data, table, changeset):
    """
    Get all the rows from a table.
    :param _config:
    :param table: The name of the table to get all rows from.
    :param changeset: The changeset containing the database connection and cursor.
    :return: The query results or an error.
    """
    try:
        cursor = changeset["changes"].get("cursor")
        cursor.execute(f"SELECT * FROM {table}")
        results = cursor.fetchall()
        return results
    except Exception as ex:
        return "error", {"db_error": str(ex)}


def get_from(_data, table, columns, changeset):
    """
    Get specific columns from a table.
    :param _config:
    :param table: The name of the table to get columns from.
    :param columns: The columns to get from the table.
    :param changeset: The changeset containing the database connection and cursor.
    :return: The query results or an error.
    """
    try:
        cursor = changeset["changes"].get("cursor")
        cursor.execute(f"SELECT {', '.join(columns)} FROM {table}")
        results = cursor.fetchall()
        return results
    except Exception as ex:
        return "error", {"db_error": str(ex)}


def get_first(_data, table, columns=None, changeset=None):
    """
    Get the first row from a table.
    :param _config:
    :param table: The name of the table to get the first row from.
    :param columns: The columns to get from the table.
    :param changeset: The changeset containing the database connection and cursor.
    :return: The query results or an error.
    """
    try:
        cursor = changeset["changes"].get("cursor")
        if columns:
            cursor.execute(f"SELECT {', '.join(columns)} FROM {table} LIMIT 1")
        else:
            cursor.execute(f"SELECT * FROM {table} LIMIT 1")
        results = cursor.fetchall()
        return results
    except Exception as ex:
        return "error", {"db_error": str(ex)}


def get_where_value_equals(_data, table, column, value, changeset):
    """
    Get rows from a table where a column has a specific value.
    :param _config:
    :param table: The name of the table to get rows from.
    :param column: The column to filter rows by.
    :param value: The value to filter rows by.
    :param changeset: The changeset containing the database connection and cursor.
    :return: The query results or an error.
    """
    try:
        cursor = changeset["changes"].get("cursor")
        cursor.execute(f"SELECT * FROM {table} WHERE {column} = '{value}'")
        results = cursor.fetchall()
        return results
    except Exception as ex:
        return "error", {"db_error": str(ex)}


def get_where(_data, table, condition, changeset):
    """
    Get rows from a table based on a condition.
    :param _config:
    :param table: The name of the table to get rows from.
    :param condition: The condition to filter rows by.
    :param changeset: The changeset containing the database connection and cursor.
    :return: The query results or an error.
    """
    try:
        cursor = changeset["changes"].get("cursor")
        cursor.execute(f"SELECT * FROM {table} WHERE {condition}")
        results = cursor.fetchall()
        return results
    except Exception as ex:
        return "error", {"db_error": str(ex)}


def close_connection(_config, changeset):
    """
    Close the connection to the database.
    :param _config:
    :param changeset:
    :return: A tuple indicating a change with the new connection and cursor, or an error.
    """
    changeset = changeset.get("changes", {})
    if changeset.get("connection") and changeset.get("cursor"):
        try:
            changeset["cursor"].close()
            changeset["connection"].close()
            del changeset["cursor"]
            del changeset["connection"]
            return None
        except Exception as ex:
            raise ex
