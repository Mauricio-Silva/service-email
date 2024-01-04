from fastapi import HTTPException


class HttpException(HTTPException):
    def __init__(self, status_code: int, message: str) -> None:
        self.success = False
        self.status_code = status_code
        self.message = message
        super().__init__(status_code, message)

    def dict(self):
        return {"success": self.success, "message": self.message}


class Unauthorized(HttpException):
    def __init__(self, message: str) -> None:
        super().__init__(401, message)


class UnsupportedMediaType(HttpException):
    def __init__(self, prefix: str) -> None:
        super().__init__(415, f"Invalid {prefix} header")


class RequiredRequestBody(HttpException):
    def __init__(self) -> None:
        super().__init__(422, "Request body is required")


class FailedDependency(HttpException):
    def __init__(self, message: str) -> None:
        super().__init__(424, message)
