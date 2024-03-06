from .api_status_error import ApiStatusError


class BadRequestError(ApiStatusError):
    """400 - Bad Request"""

    def __init__(self, response=None):
        super().__init__(status_code=400, response=response)
