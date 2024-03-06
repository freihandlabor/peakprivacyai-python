from ..exceptions.api_token_not_found_error import ApiTokenNotFoundError


class ApiKeyValidator:
    @staticmethod
    def check_api_token(api_key):
        if not api_key:
            raise ApiTokenNotFoundError("API token is missing.")
