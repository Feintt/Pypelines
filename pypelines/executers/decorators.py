class PipeExecute:
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
        # Just execute the function without modifying 'other'
        all_args = (other,) + self.params
        self.func(*all_args, **self.kwargs)
        # Return 'other' so it can be passed to the next function in the pipeline
        return other
