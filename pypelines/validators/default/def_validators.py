from pypelines.validators import PipeValidator
import re


@PipeValidator
def is_non_empty_string(value):
    return isinstance(value, str) and bool(value.strip())


@PipeValidator
def min_length(value, min_len: int):
    return isinstance(value, str) and len(value) >= min_len


@PipeValidator
def max_length(value, max_len: int):
    return isinstance(value, str) and len(value) <= max_len


@PipeValidator
def contains_substring(value, substring: str):
    return isinstance(value, str) and substring in value


@PipeValidator
def starts_with(value, prefix: str):
    return isinstance(value, str) and value.startswith(prefix)


@PipeValidator
def ends_with(value, suffix: str):
    return isinstance(value, str) and value.endswith(suffix)


@PipeValidator
def matches_pattern(value, pattern: str):
    return isinstance(value, str) and re.search(pattern, value) is not None


@PipeValidator
def is_numeric(value):
    return isinstance(value, str) and value.isdigit()


@PipeValidator
def is_alphanumeric(value):
    return isinstance(value, str) and value.isalnum()


@PipeValidator
def is_email(value):
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return isinstance(value, str) and re.match(pattern, value) is not None
