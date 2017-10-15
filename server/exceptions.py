from sanic.exceptions import SanicException


class BaseHTTPError(SanicException):
    message = ''
    code = 500

    def __init__(self, message):
        super().__init__(self)
        self.message = message

    def __dict__(self):
        return {
            'code': self.code,
            'message': self.message,
        }


class ServiceError(BaseHTTPError):
    code = 500


class InvalidQueryError(BaseHTTPError):
    code = 400


class SerializationError(BaseHTTPError):
    code = 500
