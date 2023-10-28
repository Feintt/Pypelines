class PipelineBrokenError(Exception):
    """Exception raised when a pipeline function fails."""
    pass


class PipeFunction:
    """Class used to create functions that can be pipelined using the '|' operator."""

    def __init__(self, func):
        self.func = func

    def __ror__(self, other):
        def wrapped(*args, **kwargs):
            result = other(*args, **kwargs)
            if not self.func(result):
                raise PipelineBrokenError(f"Broken pipe error in function {self.func.__name__}")
            return result

        return wrapped

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
