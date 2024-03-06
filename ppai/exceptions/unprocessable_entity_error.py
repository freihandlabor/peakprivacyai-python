from .api_status_error import ApiStatusError


class UnprocessableEntityError(ApiStatusError):
    """422 - Unprocessable Entity"""

    def __init__(self, response=None):
        super().__init__(status_code=422, response=response)
