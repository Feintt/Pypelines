import re
from jsonschema import validate, ValidationError


def validate_json_schema(data, schema):
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        return "error", {"schema": str(e)}
    return data


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


# Validates if at least one of the specified keys is present in the JSON data
def validate_any_key_present(data, keys):
    if not any(key in data for key in keys):
        return "error", {", ".join(keys): "At least one of these keys must be present."}
    return data


# Validates if the value of a specified key is one of the valid values
def validate_enum(data, key, valid_values):
    if key in data:
        if data[key] not in valid_values:
            return "error", {key: f"Value must be one of {valid_values}."}
    else:
        return "error", {key: "Key is required but missing."}
    return data


# Validates if the value of a specified key is a valid JSON object
def validate_nested_json(data, key, validation_pipeline):
    from pypelines import Pipeable
    if key in data:
        nested_result = validation_pipeline(Pipeable(data[key])).get_changeset()
        if nested_result["errors"]:
            return "error", {key: nested_result["errors"]}
    else:
        return "error", {key: "Key is required but missing."}
    return data


# Validates if the value of a specified key is a list and optionally validates the items in the list
def validate_list_items(data, key, item_type=None, validation_func=None):
    if key in data and isinstance(data[key], list):
        if item_type and not all(isinstance(item, item_type) for item in data[key]):
            return "error", {key: f"All items must be of type {item_type.__name__}."}
        if validation_func:
            for i, item in enumerate(data[key]):
                result = validation_func(item)
                if result[0] == "error":
                    return "error", {f"{key}[{i}]": result[1]}
    elif key not in data:
        return "error", {key: "Key is required but missing."}
    else:
        return "error", {key: "Value is not a list."}
    return data


# Validates if the value of a specified key is a boolean
def validate_boolean(data, key):
    if key in data:
        if not isinstance(data[key], bool):
            return "error", {key: "Value is not a boolean."}
    else:
        return "error", {key: "Key is required but missing."}
    return data


# Validates if the value of a specified key is a number
def validate_number(data, key):
    if key in data:
        if not isinstance(data[key], (int, float)):
            return "error", {key: "Value is not a number."}
    else:
        return "error", {key: "Key is required but missing."}
    return data


# Validates if the value of a specified key is a string
def validate_string(data, key):
    if key in data:
        if not isinstance(data[key], str):
            return "error", {key: "Value is not a string."}
    else:
        return "error", {key: "Key is required but missing."}
    return data


# Validates if the value of a specified key is a dictionary
def validate_dict(data, key):
    if key in data:
        if not isinstance(data[key], dict):
            return "error", {key: "Value is not a dictionary."}
    else:
        return "error", {key: "Key is required but missing."}
    return data


# Validates if the value of a specified key is a valid date
def validate_date(data, key, date_format="%Y-%m-%d"):
    from datetime import datetime
    if key in data:
        try:
            datetime.strptime(data[key], date_format)
        except ValueError as e:
            return "error", {key: str(e)}
    else:
        return "error", {key: "Key is required but missing."}
    return data


# Validate if value is a list
def validate_list(data, key):
    if key in data:
        if not isinstance(data[key], list):
            return "error", {key: "Value is not a list."}
    else:
        return "error", {key: "Key is required but missing."}
    return data


# Validate if value ia a tuple
def validate_tuple(data, key):
    if key in data:
        if not isinstance(data[key], tuple):
            return "error", {key: "Value is not a tuple."}
    else:
        return "error", {key: "Key is required but missing."}
    return data


# Validate if value is a set
def validate_set(data, key):
    if key in data:
        if not isinstance(data[key], set):
            return "error", {key: "Value is not a set."}
    else:
        return "error", {key: "Key is required but missing."}
    return data


# Validate if value is null
def validate_null(data, key):
    if key in data:
        if data[key] is not None:
            return "error", {key: "Value is not null."}
    else:
        return "error", {key: "Key is required but missing."}
    return data


# Validate if value is a function
def validate_function(data, key):
    if key in data:
        if not callable(data[key]):
            return "error", {key: "Value is not a function."}
    else:
        return "error", {key: "Key is required but missing."}
    return data


# Validate if value is an instance of a class
def validate_instance(data, key, class_type):
    if key in data:
        if not isinstance(data[key], class_type):
            return "error", {key: f"Value is not an instance of {class_type.__name__}."}
    else:
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
