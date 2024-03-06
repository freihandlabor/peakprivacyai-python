from .model import Model


class ModelList:
    def __init__(self, data):
        models = []
        if data:
            models = [Model(id=model_data["id"],
                            created=model_data["created"],
                            max_tokens=model_data["max_tokens"],
                            object=model_data["object"],
                            owned_by=model_data["owned_by"]) for model_data in data]
        self.models = models

    def __str__(self):
        attributes = vars(self)
        attribute_strings = []
        for key, value in attributes.items():
            if isinstance(value, str):
                # If the value is a string, include quotes around it
                value_str = f"{key}='{value}'"
            else:
                # For other types, include the value as is
                value_str = f"{key}={value}"
            attribute_strings.append(value_str)
        return f"ModelList({', '.join(attribute_strings)})"

    def __repr__(self):
        return str(self)
