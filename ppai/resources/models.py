from ..utils.http_client import HttpClient

from ..types.model_list import ModelList

from ..exceptions.api_connection_error import ApiConnectionError


class Models:
    def __init__(self, pp_ai_instance):
        self.__api_url = pp_ai_instance.get_api_url()
        self.__api_token = pp_ai_instance.get_api_token()

    def list(self):
        http_client = HttpClient(self.__api_url, self.__api_token)
        response = http_client.request("GET", "ai/models")

        try:
            return ModelList(response['data'])
        except Exception as e:
            raise ApiConnectionError()
