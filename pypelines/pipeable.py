class Pipeable:
    def __init__(self, value):
        self.value = value
        # Initialize changeset with two keys for organization
        self.changeset = {"changes": {}, "errors": {}}

    def add_error(self, error_dict):
        for key, message in error_dict.items():
            if key not in self.changeset["errors"]:
                self.changeset["errors"][key] = []
            self.changeset["errors"][key].append(message)

    def get_changeset(self):
        # Method to access the changeset
        return self.changeset

    def __or__(self, func):
        if func == print:
            print(self.value)
            return self
        elif callable(func):
            result = func(self.value)  # Execute the provided function
            # Check if the result indicates an error
            if isinstance(result, tuple) and result[0] == "error":
                self.add_error(result[1])
            # No else needed; we no longer create a new Pipeable instance
            return self  # Always return the current instance
        elif isinstance(func, tuple) and callable(func[0]):
            function, *args = func
            # Execute the provided function with additional arguments
            result = function(self.value, *args)
            if isinstance(result, tuple) and result[0] == "error":
                self.add_error(result[1])
            return self  # Always return the current instance
        else:
            raise ValueError("Right operand must be callable or a tuple with a callable as the first element")

    def __repr__(self):
        return f"Pipeable(value={self.value}, changeset={self.changeset})"
