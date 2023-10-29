class PipeValidatorBrokenError(Exception):
    """Exception raised when a pipeline function fails."""
    pass


class PipeValidator:
    """Class used to create functions that can be pipelined using the '|' operator."""

    def __init__(self, func):
        self.func = func

    def __ror__(self, other):
        # Check if 'other' is callable (a function) or a simple value
        if callable(other):
            # If it's a function, you keep the current behavior
            def wrapped(*args, **kwargs):
                result = other(*args, **kwargs)
                if not self.func(result):
                    raise PipeValidatorBrokenError(f"Broken pipe error in function {self.func.__name__}")
                return result

            return wrapped
        else:
            # If it's a value, you directly apply your function to the value
            result = other  # In this case, 'other' is a simple value, not a function
            if not self.func(result):
                raise PipeValidatorBrokenError(f"Broken pipe error in function {self.func.__name__}")
            return result

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
