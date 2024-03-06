from .api_status_error import ApiStatusError


class NotFoundError(ApiStatusError):
    """404 - Not Found"""

    def __init__(self, response=None):
        super().__init__(status_code=404, response=response)
