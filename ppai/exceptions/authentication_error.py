from .api_status_error import ApiStatusError


class AuthenticationError(ApiStatusError):
    """401 - Authentication Error"""

    def __init__(self, response=None):
        super().__init__(status_code=401, response=response)
