class Pipeable:
    def __init__(self, value):
        self.value = value
        # Initialize changeset with two keys for organization
        self.changeset = {"changes": {}, "errors": {}}

    def add_error(self, key, message):
        # Check if the key already exists, if not initialize as a list
        if key not in self.changeset["errors"]:
            self.changeset["errors"][key] = []
        # Append the new error message to the list under the key
        self.changeset["errors"][key].append(message)

    def get_changeset(self):
        # Method to access the changeset
        return self.changeset

    def __or__(self, func):
        if func == print:
            print(self.value)
            return self  # Return self to maintain the chain with the current state
        elif callable(func):
            result = func(self.value)  # Call the function with the current value
            if isinstance(result, dict) and "error" in result:
                # If the result is a dict containing an error, update the changeset
                error_message = result["error"]
                # Assuming you want a generic error key or some logic to generate a unique key
                self.add_error("error", error_message)
                return self  # Return self to continue the chain even after an error
            else:
                # If no error, update the value with the result and return a new Pipeable object
                return Pipeable(result)
        elif isinstance(func, tuple) and callable(func[0]):
            function, *args = func
            args = (self.value, *args)  # Ensure the first argument is always the current value
            result = function(*args)
            if isinstance(result, dict) and "error" in result:
                error_message = result["error"]
                self.add_error("error", error_message)
                return self
            else:
                return Pipeable(result)
        else:
            raise ValueError("Right operand must be callable or a tuple with a callable as the first element")

    def __repr__(self):
        return f"Pipeable(value={self.value}, changeset={self.changeset})"
