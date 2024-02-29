class Pipeable:
    def __init__(self, value):
        self.value = value
        self.changeset = {"changes": {}, "errors": {}}

    def add_error(self, error_dict):
        for key, message in error_dict.items():
            if key not in self.changeset["errors"]:
                self.changeset["errors"][key] = []
            self.changeset["errors"][key].append(message)

    def add_change(self, change_dict):
        for key, change in change_dict.items():
            self.changeset["changes"][key] = change

    def get_changeset(self):
        return self.changeset

    def __or__(self, operation):
        if operation == print:
            print(self.value)
            return self

        if isinstance(operation, tuple):
            func, *args = operation  # Unpack the function and its arguments
            # Process each argument, checking for nested keys
            processed_args = [self.get_nested_value(arg) if isinstance(arg, str) and '.' in arg else arg for arg in
                              args]
            args = [self.value, *processed_args]  # Include self.value as the first argument
        else:
            func = operation
            args = [self.value]  # Use self.value as the only argument if no additional args are specified

        # Append the changeset as the last argument
        args_with_changeset = [*args, self.changeset]

        try:
            result = func(*args_with_changeset)
        except Exception as e:
            print(f"Error during pipeline operation: {e}")
            return self

        if isinstance(result, tuple):
            action, data = result
            if action == "error":
                self.add_error(data)
            elif action == "change":
                self.add_change(data)
        elif result is not None:
            self.value = result

        return self

    def __repr__(self):
        return f"Pipeable(value={self.value}, changeset={self.changeset})"

    def get_nested_value(self, nested_key):
        keys = nested_key.split(".")
        value = self.value
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                # Optionally, handle missing key more gracefully or log an error
                return None
        return value
