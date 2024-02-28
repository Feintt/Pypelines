from pypelines import Pipeable
from pypelines.json_validation import *


# Additional validation functions for the preferences and address
def validate_preferences(data, key):
    newsletter_options = ["daily", "weekly", "monthly"]
    valid_themes = ["technology", "health", "sports", "entertainment"]

    preferences = data.get(key, {})
    errors = {}

    # Validate newsletter frequency
    newsletter_freq = preferences.get("newsletter")
    if newsletter_freq not in newsletter_options:
        errors["newsletter"] = "Invalid newsletter frequency."

    # Validate themes
    themes = preferences.get("themes", [])
    if not all(theme in valid_themes for theme in themes):
        errors["themes"] = "Contains invalid theme(s)."

    if errors:
        return "error", {key: errors}
    return data


def validate_address(data, key):
    required_keys = ["street", "city", "zip"]
    missing_keys = [k for k in required_keys if k not in data.get(key, {})]
    if missing_keys:
        return "error", {key: {k: "This key is missing." for k in missing_keys}}
    return data


# Test JSON
test_json = {
    "name": "Jane Doe",
    "age": 25,
    "email": "jane.doe@example.com",
    "is_subscribed": True,
    "preferences": {
        "newsletter": "weekly",
        "themes": ["technology", "health"]
    },
    "address": {
        "street": "123 Elm St",
        "city": "Springfield",
        "zip": "12345"
    }
}

# Validation Pipeline
result = (Pipeable(test_json)
          | (validate_required_fields, ["name", "age", "email", "is_subscribed", "preferences", "address"])
          | (validate_email, "email")
          | (validate_numeric_range, "age", 18, 99)
          | (validate_boolean, "is_subscribed")
          | (validate_preferences, "preferences")
          | (validate_address, "address")
          )

# Output the result
print(result.get_changeset())
