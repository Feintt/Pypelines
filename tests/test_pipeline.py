from pypelines.pipeable import Pipeable
import re  # Regular expression module

test_json = {
    "name": "John Doe",
    "age": 11,
    "city": "New York"
}


def validate_contains(data, key):
    if key not in data:
        return {"error": f"Key '{key}' not found in data"}
    return data


def validate_key_type(data, key, expected_type):
    if not isinstance(data.get(key, None), expected_type):
        return {"error": f"Value for '{key}' is not of type {expected_type.__name__}"}
    return data


def validate_length(data, key, expected_length):
    value = data.get(key, None)
    if value is None or len(value) != expected_length:
        return {"error": f"Length of '{key}' is not {expected_length}"}
    return data


def validate_min_value(data, key, min_value):
    if data.get(key, None) is None or data[key] < min_value:
        return {"error": f"Value for '{key}' is less than minimum allowed value of {min_value}"}
    return data


def validate_max_value(data, key, max_value):
    if data.get(key, None) is None or data[key] > max_value:
        return {"error": f"Value for '{key}' exceeds maximum allowed value of {max_value}"}
    return data


def validate_email_format(data, key):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(pattern, data.get(key, '')):
        return {"error": f"Value for '{key}' is not a valid email address"}
    return data


result = (Pipeable(test_json)
          | (validate_contains, "name")
          | (validate_key_type, "name", str)
          | (validate_length, "name", 8)
          | (validate_contains, "age")
          | (validate_key_type, "age", int)
          | (validate_min_value, "age", 18)
          | (validate_contains, "email")
          | (validate_email_format, "email")
          )

print(result.get_changeset())
