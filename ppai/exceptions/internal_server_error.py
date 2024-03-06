from .api_status_error import ApiStatusError


class InternalServerError(ApiStatusError):
    """>=500 - Internal Server Error"""

    def __init__(self, response=None):
        super().__init__(status_code=500, response=response)
