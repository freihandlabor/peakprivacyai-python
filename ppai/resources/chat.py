from ..utils.http_client import HttpClient

from ..types.api_token_valid import ApiTokenValid
from .completions import Completions

from ..exceptions.api_connection_error import ApiConnectionError


class Chat:
    def __init__(self, pp_ai_instance):
        self.__api_url = pp_ai_instance.get_api_url()
        self.__api_token = pp_ai_instance.get_api_token()
        self.completions = Completions(pp_ai_instance)

    def check_api_token(self):
        http_client = HttpClient(self.__api_url, self.__api_token)
        http_client.request("GET", "ai/ping")

        try:
            return ApiTokenValid()
        except Exception as e:
            raise ApiConnectionError()
