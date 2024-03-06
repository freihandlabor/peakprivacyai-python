from .api_status_error import ApiStatusError


class RateLimitError(ApiStatusError):
    """429 - Rate Limit Exceeded"""

    def __init__(self, response=None):
        super().__init__(status_code=429, response=response)
