import os as os
from dotenv import load_dotenv

# load env file
load_dotenv()

# Validators
from .validators.api_token_validator import ApiKeyValidator

# Resources
from .resources.models import Models
from .resources.chat import Chat


class PpAi:
    def __init__(self, api_token: str | None = None):
        if api_token is None:
            api_token = os.environ.get("PPAI_API_TOKEN")
        ApiKeyValidator.check_api_token(api_token)

        self.__api_token = api_token
        self.__api_url = "https://api.peakprivacy.ch/v1/"
        if os.environ.get("PPAI_API_URL") is not None:
            self.__api_url = os.environ.get("PPAI_API_URL")

        self.models = Models(self)
        self.chat = Chat(self)

    def get_api_url(self):
        return self.__api_url

    def get_api_token(self):
        return self.__api_token
