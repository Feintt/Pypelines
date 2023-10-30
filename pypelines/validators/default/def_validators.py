from pypelines.validators import PipeValidator
import re


@PipeValidator
def is_non_empty_string(value):
    return isinstance(value, str) and bool(value.strip())


@PipeValidator
def is_non_empty_string_or_none(value):
    return isinstance(value, str) and (not value or bool(value.strip()))


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


@PipeValidator
def is_url(value):
    pattern = r"(http|https)://[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    return isinstance(value, str) and re.match(pattern, value) is not None


@PipeValidator
def is_phone_number(value):
    pattern = r"^\+?[0-9]{10,}$"
    return isinstance(value, str) and re.match(pattern, value) is not None


@PipeValidator
def is_integer(value):
    return isinstance(value, str) and value.isdigit()


@PipeValidator
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


@PipeValidator
def is_boolean(value):
    return isinstance(value, bool)


@PipeValidator
def is_list(value):
    return isinstance(value, list)


@PipeValidator
def is_dict(value):
    return isinstance(value, dict)


@PipeValidator
def is_tuple(value):
    return isinstance(value, tuple)


@PipeValidator
def is_set(value):
    return isinstance(value, set)


@PipeValidator
def is_frozenset(value):
    return isinstance(value, frozenset)


@PipeValidator
def is_none(value):
    return value is None


@PipeValidator
def is_not_none(value):
    return value is not None


@PipeValidator
def is_in(value, container: list):
    return value in container


@PipeValidator
def is_not_in(value, container: list):
    return value not in container


@PipeValidator
def is_in_range(value, start: int, end: int):
    return start <= value <= end


@PipeValidator
def is_not_in_range(value, start: int, end: int):
    return not start <= value <= end


@PipeValidator
def is_greater_than(value, other: int):
    return value > other


@PipeValidator
def is_greater_than_or_equal(value, other: int):
    return value >= other


@PipeValidator
def is_less_than(value, other: int):
    return value < other


@PipeValidator
def is_less_than_or_equal(value, other: int):
    return value <= other


@PipeValidator
def is_equal(value, other):
    return value == other


@PipeValidator
def is_not_equal(value, other):
    return value != other


@PipeValidator
def is_empty(value):
    return not value


@PipeValidator
def is_not_empty(value):
    return bool(value)


@PipeValidator
def is_true(value):
    return value is True


@PipeValidator
def is_false(value):
    return value is False


@PipeValidator
def is_truthy(value):
    return bool(value)


@PipeValidator
def is_falsy(value):
    return not bool(value)


@PipeValidator
def is_instance_of(value, cls):
    return isinstance(value, cls)


@PipeValidator
def is_not_instance_of(value, cls):
    return not isinstance(value, cls)


@PipeValidator
def is_subclass_of(value, cls):
    return issubclass(value, cls)


@PipeValidator
def is_not_subclass_of(value, cls):
    return not issubclass(value, cls)


@PipeValidator
def is_callable(value):
    return callable(value)


@PipeValidator
def is_not_callable(value):
    return not callable(value)


@PipeValidator
def is_iterable(value):
    return hasattr(value, "__iter__")


@PipeValidator
def is_not_iterable(value):
    return not hasattr(value, "__iter__")


@PipeValidator
def is_iterator(value):
    return hasattr(value, "__next__")


@PipeValidator
def is_not_iterator(value):
    return not hasattr(value, "__next__")
