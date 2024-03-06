import json

from ..utils.http_client import HttpClient
from typing import Optional

from ..types.stream import Stream
from ..types.chat_completion import ChatCompletion

from ..exceptions.api_connection_error import ApiConnectionError


class Completions:
    def __init__(self, pp_ai_instance):
        self.__api_url = pp_ai_instance.get_api_url()
        self.__api_token = pp_ai_instance.get_api_token()

    def create(self,
               messages,
               model,
               anonymize: Optional[bool] = None,
               max_tokens: Optional[int] = None,
               random_seed: Optional[int] = None,
               safe_prompt: Optional[bool] = None,
               temperature: Optional[float] = None,
               top_p: Optional[float] = None,
               stream: Optional[bool] = False,
               ):
        payload_data = {
            "messages": messages,
            "model": model,
            "anonymize": anonymize,
            "max_tokens": max_tokens,
            "random_seed": random_seed,
            "safe_prompt": safe_prompt,
            "temperature": temperature,
            "top_p": top_p,
            "stream": stream
        }

        http_client = HttpClient(self.__api_url, self.__api_token)
        response = http_client.request("POST", "ai/completions", payload_data=payload_data, stream=stream)

        try:
            if stream is True:
                return Stream(response)
            else:
                return ChatCompletion(response)
        except Exception as e:
            raise ApiConnectionError()
