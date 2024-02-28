"""
This module contains functions that modify strings using the pipeable pattern.
"""
from pypelines.pipeable import Pipeable
import re


def to_upper(value):
    """
    Converts a string to uppercase.
    """
    return value.upper()


def to_lower(value):
    """
    Converts a string to lowercase.
    """
    return value.lower()


def capitalize(value):
    """
    Capitalizes the first letter of a string.
    """
    return value.capitalize()


def replace(value, old, new):
    """
    Replaces a substring with another substring in a string.
    """
    return value.replace(old, new)


def split(value, separator):
    """
    Splits a string into a list of strings using a separator.
    """
    return value.split(separator)


def join(value, separator):
    """
    Joins a list of strings into a single string using a separator.
    """
    return separator.join(value)


def strip(value):
    """
    Strips leading and trailing whitespace from a string.
    """
    return value.strip()


def lstrip(value):
    """
    Strips leading whitespace from a string.
    """
    return value.lstrip()


def rstrip(value):
    """
    Strips trailing whitespace from a string.
    """
    return value.rstrip()


def contains(value, substring):
    """
    Checks if the string contains the specified substring.
    """
    if substring in value:
        return value
    else:
        return "error", {"contains": f"Substring '{substring}' not found"}


def starts_with(value, prefix):
    """
    Checks if the string starts with the specified prefix.
    """
    if value.startswith(prefix):
        return value
    else:
        return "error", {"starts_with": f"String does not start with '{prefix}'"}


def ends_with(value, suffix):
    """
    Checks if the string ends with the specified suffix.
    """
    if value.endswith(suffix):
        return value
    else:
        return "error", {"ends_with": f"String does not end with '{suffix}'"}


def match(value, pattern):
    """
    Checks if the string matches the specified regular expression pattern.
    """
    if re.match(pattern, value):
        return value
    else:
        return "error", {"match": f"String does not match pattern '{pattern}'"}


def regex_search(value, pattern):
    """
    Searches for a pattern using regex and returns the match.
    """
    return re.search(pattern, value)


def regex_replace(value, pattern, repl):
    """
    Replaces occurrences of a pattern with a replacement string.
    """
    return re.sub(pattern, repl, value)


def regex_split(value, pattern):
    """
    Splits the string by a regex pattern.
    """
    return re.split(pattern, value)


def pad_left(value, width, fillchar=' '):
    """
    Left pads the string to a specified width.
    """
    return value.rjust(width, fillchar)


def pad_right(value, width, fillchar=' '):
    """
    Right pads the string to a specified width.
    """
    return value.ljust(width, fillchar)


def pad_both(value, width, fillchar=' '):
    """
    Pads the string on both sides to a specified width.
    """
    return value.center(width, fillchar)


def to_snake_case(value):
    """
    Converts a string to snake_case.
    """
    return '_'.join(
        re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', value.replace('-', ' '))).split()).lower()


def to_camel_case(value):
    """
    Converts a string to camelCase.
    """
    parts = value.split('_')
    return parts[0] + ''.join(x.capitalize() or '_' for x in parts[1:])


def to_kebab_case(value):
    """
    Converts a string to kebab-case.
    """
    return value.lower().replace('_', '-')
