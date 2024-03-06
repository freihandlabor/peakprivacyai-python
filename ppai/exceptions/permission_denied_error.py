from .api_status_error import ApiStatusError


class PermissionDeniedError(ApiStatusError):
    """403 - Permission Denied"""

    def __init__(self, response=None):
        super().__init__(status_code=403, response=response)
