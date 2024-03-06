from .stream_choice import StreamChoice


class ChatCompletionChunk:
    def __init__(self, content):
        self.id = content['id']
        self.choices = [StreamChoice(content['choices'][0])]
        self.created = content['created']
        self.model = content['model']
        self.object = content['object']

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
        return f"ChatCompletionChunk({', '.join(attribute_strings)})"

    def __repr__(self):
        return str(self)
