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

    def add_change(self, change_dict):
        for key, change in change_dict.items():
            # Assume changes are to be overwritten or added, not appended like errors
            self.changeset["changes"][key] = change

    def get_changeset(self):
        # Method to access the changeset
        return self.changeset

    def __or__(self, operation):
        if operation == print:
            print(self.value)
            return self

        func, *args = (operation if isinstance(operation, tuple) else (operation,))

        processed_args = []
        for arg in args:
            if isinstance(arg, str) and "." in arg:
                processed_arg = self.get_nested_value(arg)
                if processed_arg is None:
                    print(f"Warning: Nested key '{arg}' not found.")
                    return self
                processed_args.append(processed_arg)
            else:
                processed_args.append(arg)

        if callable(func):
            result = func(self.value, *processed_args)
            if isinstance(result, tuple):
                if result[0] == "error":
                    self.add_error(result[1])
                elif result[0] == "change":
                    self.add_change(result[1])
            elif result is not None:
                self.value = result
            return self
        else:
            raise ValueError("Operation must be callable or a tuple with a callable as the first element")

    def get_nested_value(self, nested_key):
        """
        Fetches a value from a nested dictionary using dot notation.
        """
        keys = nested_key.split(".")
        value = self.value
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                # Handle missing key or value is not a dict; return a specific error or None
                return None  # or raise an error
        return value

    def __repr__(self):
        return f"Pipeable(value={self.value}, changeset={self.changeset})"
