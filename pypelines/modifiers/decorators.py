class NullPipeBrokenError(Exception):
    """Exception raised when a Null value is passed to a pipe."""
    pass


class PipeModifier:
    def __init__(self, func):
        self.func = func

    def __ror__(self, other):
        return self.func(other)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
