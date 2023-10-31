class PipeValidatorError(Exception):
    """Exception raised when a pipeline function fails."""
    pass


class UnknownPipeValidatorError(Exception):
    """Exception raised when a pipeline function fails due to an unknown error."""
    pass


class PipeValidator:
    """
    Decorator class for pipeline functions.

    This decorator can be used to decorate functions that are used in pipelines
    to validate the input. The pipe will break if the function returns
    False, None or an Exception.
    If the function returns True or anything else, the pipe will pass the input
    to the next stage in the pipeline.

    :param func: The function to be decorated.
    :param unpack: Whether to unpack the input or not.
    :return: The decorated function.
    """

    def __init__(self, func=None, unpack=False, skip=True):
        self.func = func
        self.unpack = unpack
        self.params = ()
        self.kwargs = {}
        self.skip = skip

    def __call__(self, *args, **kwargs):
        if self.func is None:
            # If we're here, __call__ was used like __init__, i.e., this is a decorator with parameters.
            self.func = args[0]  # the function being decorated is the only positional arg
            return self  # it's crucial to return the instance itself to keep the chain operable.
        else:
            # Here, we're called like a regular function, so we behave like one.
            self.params = args
            self.kwargs = kwargs
            return self

    def __ror__(self, other):
        # The __ror__ method is called with the "|" operator. 'Other' is the left-hand operand.
        # try:
        # Determine whether to unpack 'other' based on its type and the 'unpack' flag.
        if self.unpack and isinstance(other, tuple):
            all_args = *other, *self.params  # Unpack 'other' if it's a tuple and combine it with 'self.params'.
        else:
            all_args = (other,) + self.params  # Keep 'other' as is.

        # Call the actual function with the prepared arguments and keyword arguments.
        result = self.func(*all_args, **self.kwargs)

        # Validate the result of the function call.
        if not result or isinstance(result, Exception) or result is None:
            raise PipeValidatorError(f"Validation failed in function {self.func.__name__}")

        if self.skip:
            return other
        return result
