from pypelines import Pipeable
from pypelines.json_validation import *

test_json = {
    "name": "John Doe",
    "age": 9,
    "city": "New York",
    "email": "test@test.com"
}

result = (Pipeable(test_json)
          | (validate_required_fields, ["name", "age", "city", "email"])
          | (validate_data_type, "name", str)
          | (validate_data_type, "age", int)
          | (validate_data_type, "city", str)
          | (validate_string_length, "name", 3, 50)
          | (validate_numeric_range, "age", 0, 120)
          | (validate_string_length, "city", 3, 50)
          )

print(result.changeset)
