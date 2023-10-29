class PipeValidatorBrokenError(Exception):
    """Exception raised when a pipeline function fails."""
    pass


class UnknownPipeValidatorError(Exception):
    """Exception raised when a pipeline function fails due to an unknown error."""
    pass


class PipeValidator:
    """Class used to create functions that can be pipelined using the '|' operator."""

    def __init__(self, func):
        self.func = func
        self.params = ()
        self.kwargs = {}

    def __call__(self, *args, **kwargs):
        # This is called if the instance itself is called like a function.
        # Here, we're storing the extra arguments and keyword arguments to be used later.
        self.params = args
        self.kwargs = kwargs
        return self  # It's crucial to return the instance itself so the __ror__ can be called later.

    def __ror__(self, other):
        # The __ror__ method is called with the "|" operator. 'Other' is the left-hand operand.
        try:
            # We prepare arguments by combining 'other' with self.params. 'Other' becomes the first argument.
            all_args = (other,) + self.params

            # Call the actual function with the prepared arguments and keyword arguments.
            result = self.func(*all_args, **self.kwargs)
            if not result:
                raise PipeValidatorBrokenError(f"Broken pipe error in function {self.func.__name__}")

        except PipeValidatorBrokenError as e:
            raise e
        except Exception as e:
            raise UnknownPipeValidatorError(f"Unknown error in function {self.func.__name__}: {e}") from e

        return other  # The result can be used as input for the next stage in the pipeline.
