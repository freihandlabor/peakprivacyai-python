class ChatCompletionMessage:
    def __init__(self, content, role):
        self.content = content
        self.role = role

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
        return f"ChatCompletionMessage({', '.join(attribute_strings)})"

    def __repr__(self):
        return str(self)
