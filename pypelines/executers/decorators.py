class PipeExecute:
    def __init__(self, func=None, unpack=False):
        self.func = func
        self.unpack = unpack
        self.params = ()
        self.kwargs = {}

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
        # Determine whether to unpack 'other' based on its type and the 'unpack' flag.
        if self.unpack and isinstance(other, tuple) or self.unpack and isinstance(other, list) or self.unpack and isinstance(other, set):
            all_args = *other, *self.params  # Unpack 'other' if it's a tuple and combine it with 'self.params'.
        else:
            all_args = (other,) + self.params  # Keep 'other' as is.

        # Execute the function with the constructed arguments. The function's result is ignored to maintain the
        # pipeline's data flow.
        self.func(*all_args, **self.kwargs)

        # Return 'other' so it can be passed to the next function in the pipeline without modification.
        return other
