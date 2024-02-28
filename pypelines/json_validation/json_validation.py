import re


# Validates if the specified key is a valid email address
def validate_email(data, key):
    if key in data and isinstance(data[key], str):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", data[key]):
            return "error", {key: "Value is not a valid email address."}
    elif key not in data:
        return "error", {key: "Key is required but missing."}
    return data


# Validates if the specified keys are present in the JSON data
def validate_required_fields(data, required_keys):
    missing_keys = [key for key in required_keys if key not in data]
    if missing_keys:
        return "error", {key: "Key is required but missing." for key in missing_keys}
    return data


# Validates if the value of a specified key matches the expected data type
def validate_data_type(data, key, expected_type):
    if key in data and not isinstance(data[key], expected_type):
        return "error", {key: f"Expected type {expected_type.__name__}, got {type(data[key]).__name__}"}
    elif key not in data:
        return "error", {key: "Key is required but missing."}
    return data


# Validates the length of a string value for the specified key
def validate_string_length(data, key, min_length=None, max_length=None):
    if key in data and isinstance(data[key], str):
        if min_length is not None and len(data[key]) < min_length:
            return "error", {key: f"String length is shorter than the minimum length of {min_length}."}
        if max_length is not None and len(data[key]) > max_length:
            return "error", {key: f"String length exceeds the maximum length of {max_length}."}
    elif key not in data:
        return "error", {key: "Key is required but missing."}
    return data


# Validates if the value of a specified key matches a regular expression pattern
def validate_pattern(data, key, pattern):
    if key in data and isinstance(data[key], str):
        if not re.match(pattern, data[key]):
            return "error", {key: "Value does not match the required pattern."}
    elif key not in data:
        return "error", {key: "Key is required but missing."}
    return data


# Validates if a numeric value falls within a specified range
def validate_numeric_range(data, key, min_value=None, max_value=None):
    if key in data and isinstance(data[key], (int, float)):
        if min_value is not None and data[key] < min_value:
            return "error", {key: f"Value is less than the minimum allowed value of {min_value}."}
        if max_value is not None and data[key] > max_value:
            return "error", {key: f"Value exceeds the maximum allowed value of {max_value}."}
    elif key not in data:
        return "error", {key: "Key is required but missing."}
    return data


# Example of a more complex validation that depends on the values of multiple fields
def validate_date_range(data, start_date_key, end_date_key, date_format="%Y-%m-%d"):
    from datetime import datetime
    errors = {}
    try:
        if start_date_key in data and end_date_key in data:
            start_date = datetime.strptime(data[start_date_key], date_format)
            end_date = datetime.strptime(data[end_date_key], date_format)
            if start_date > end_date:
                errors[start_date_key] = "Start date must be before the end date."
                errors[end_date_key] = "End date must be after the start date."
    except ValueError as e:
        errors[start_date_key] = str(e)
        errors[end_date_key] = str(e)

    if errors:
        return "error", errors
    return data
