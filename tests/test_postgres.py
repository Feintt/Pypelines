from pypelines import Pipeable
from pypelines.postgres.config import *

postgres_config = {
    "user": "admin",
    "password": "admin",
    "host": "localhost",
    "port": 5432,
    "database": "simple_chat_dev"
}


def print_with_format(data):
    for user in data:
        print(f"User: {user}")
    return data


result = (Pipeable(postgres_config)
          | start_connection
          | (get_all, "users")
          | print_with_format
          | close_connection
          )

print(result.get_changeset())
