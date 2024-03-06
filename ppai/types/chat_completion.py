from .chat_completion_message import ChatCompletionMessage
from .choice import Choice
from .completion_usage import CompletionUsage


class ChatCompletion:
    def __init__(self, response_data):
        message_data = response_data['choices'][0]['message']
        choice_data = response_data['choices'][0]
        usage_data = response_data['usage']

        message = ChatCompletionMessage(content=message_data['content'], role=message_data['role'])
        choice = Choice(finish_reason=choice_data['finish_reason'], index=choice_data['index'], message=message)
        usage = CompletionUsage(completion_tokens=usage_data['completion_tokens'],
                                prompt_tokens=usage_data['prompt_tokens'],
                                total_tokens=usage_data['total_tokens'])

        self.id = response_data['id']
        self.choices = [choice]
        self.created = response_data['created']
        self.model = response_data['model']
        self.object = response_data['object']
        self.usage = usage

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
        return f"ChatCompletion({', '.join(attribute_strings)})"

    def __repr__(self):
        return str(self)
