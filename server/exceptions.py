from sanic.exceptions import SanicException


class BaseHTTPError(SanicException):
    message = ''
    status_code = 500

    def __init__(self, message):
        super().__init__(self)
        self.message = message

    def __dict__(self):
        return {
            'status_code': self.status_code,
            'message': self.message,
        }


class ServiceError(BaseHTTPError):
    status_code = 500


class InvalidQueryError(BaseHTTPError):
    status_code = 400


class SerializationError(BaseHTTPError):
    status_code = 500
