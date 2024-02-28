from pypelines import Pipeable
from pypelines.json_validation import *
from datetime import datetime

# Define validation functions here...

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


def validate_interests(data, key):
    valid_interests = ["tech", "music", "books", "sports", "travel"]
    interests = data.get(key, {}).get("interests", [])
    invalid_interests = [interest for interest in interests if interest not in valid_interests]
    if invalid_interests:
        return "error", {key: f"Invalid interests: {', '.join(invalid_interests)}"}
    return data


def validate_future_date(data, key, date_format="%Y-%m-%d"):
    today = datetime.now().date()
    try:
        date_value = datetime.strptime(data[key], date_format).date()
        if date_value > today:
            return "error", {key: "Date cannot be in the future."}
    except ValueError as e:
        return "error", {key: str(e)}
    return data


result = (Pipeable(test_json)
          | (validate_required_fields, ["username", "password", "email", "age", "preferences", "registration_date"])
          | (validate_email, "email")
          | (validate_string_length, "password", 8, 16)
          | (validate_numeric_range, "age", 18, 99)
          | (validate_enum, "preferences.newsletter", ["daily", "weekly", "monthly"])
          | (validate_interests, "preferences")
          | (validate_date, "registration_date")
          | (validate_future_date, "registration_date")
          )

# Output the result
print(result.get_changeset())
