from .api_error import ApiError


class ApiStatusError(ApiError):
    """Raised when the API returns a non-success status code."""

    def __init__(self, status_code=None, response=None):
        self.status_code = status_code or 500
        self.response = response
        self.message = self.get_default_message(status_code=status_code)
        super().__init__(f"API Status Error: Status {self.status_code}: {response or self.message}")

    def get_default_message(self, status_code):
        DEFAULT_MESSAGES = {
            400: "Bad Request",
            401: "Authentication Error",
            403: "Permission Denied",
            404: "Not Found",
            422: "Unprocessable Entity",
            429: "Rate Limit Exceeded",
            500: "Internal Server Error"
        }
        return DEFAULT_MESSAGES.get(status_code, f"Unknown Error for status code {status_code}")
