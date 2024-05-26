class HttpException(Exception):
    def __init__(self, status_code, message) -> None:
        self.status_code = status_code
        self.message = message


class UnprocessableEntity(HttpException):
    def __init__(self, message) -> None:
        super().__init__(status_code=422, message=message)
