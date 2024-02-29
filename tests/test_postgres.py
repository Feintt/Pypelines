from pypelines import Pipeable
from pypelines.postgres.config import *

postgres_config = {
    "user": "admin",
    "password": "admin",
    "host": "localhost",
    "port": 5432,
    "database": "simple_chat_dev"
}


def print_with_format(data, _changeset):
    for user in data:
        print(f"User: {user}")
    return data


result = (Pipeable(postgres_config)
          | start_connection
          | (get_first, "users", ["id"])
          | (get_where_value_equals, "users", "id", "16e2aad3-2d9f-43e2-ae5b-10cc09c61bdd")
          | close_connection
          )
