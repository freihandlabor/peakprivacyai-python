from .api_error import ApiError


class ApiConnectionError(ApiError):
    """Raised when unable to connect to the API."""
    DEFAULT_MESSAGE = "Unable to connect to the API"

    def __init__(self, status_code=None, response=None):
        self.status_code = status_code
        self.response = response
        super().__init__(f"API Connection Error: Status {status_code}: {response or self.DEFAULT_MESSAGE}")
