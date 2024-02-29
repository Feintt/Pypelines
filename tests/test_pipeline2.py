from pypelines import Pipeable
from pypelines.json_validation import *
from datetime import datetime

# Validation Pipeline
test_json = {
    "username": "newuser123",
    "password": "password123",
    "email": "newuser@example.com",
    "age": 29,
    "preferences": {
        "newsletter": "daily",
        "interests": ["tech", "music", "books"]
    },
    "registration_date": "2023-01-30"
}


def validate_interests(data, key, _changeset):
    valid_interests = ["tech", "music", "books", "sports", "travel"]
    interests = data.get(key, {}).get("interests", [])
    invalid_interests = [interest for interest in interests if interest not in valid_interests]
    if invalid_interests:
        return "error", {key: f"Invalid interests: {', '.join(invalid_interests)}"}
    return data


def validate_future_date(data, key, date_format="%Y-%m-%d", _changeset=None):
    today = datetime.now().date()
    try:
        date_value = datetime.strptime(data[key], date_format).date()
        if date_value > today:
            return "error", {key: "Date cannot be in the future."}
    except ValueError as e:
        return "error", {key: str(e)}
    return data


def validate_value(data, value, list_of_values, _changeset=None):
    if value not in list_of_values:
        return "error", {value: f"Value is not in the list of valid values: {', '.join(list_of_values)}"}
    return data


result = (Pipeable(test_json)
          | (validate_required_fields, ["username", "password", "email", "age", "preferences", "registration_date"])
          | (validate_email, "email")
          | (validate_string_length, "password", 8, 16)
          | (validate_numeric_range, "age", 18, 99)
          | (validate_value, "preferences.newsletter", ["daily", "weekly", "monthly"])
          | (validate_interests, "preferences")
          | (validate_date, "registration_date", "%Y-%m-%d")
          | (validate_future_date, "registration_date", "%Y-%m-%d")
          )

# Output the result
print(result.get_changeset())
