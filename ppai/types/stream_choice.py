from .model import Model
from .choice_delta import ChoiceDelta as Choice


class StreamChoice():
    def __init__(self, content):
        self.delta = Choice(
            content=content['message']['content'],
            role=content['message']['role'],
        )
        self.finish_reason = content['finish_reason']
        self.index = content['index']

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
        return f"Choice({', '.join(attribute_strings)})"

    def __repr__(self):
        return str(self)
