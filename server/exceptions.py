from sanic.exceptions import ServerError, InvalidUsage


class ServiceError(ServerError):
    pass


class InvalidQueryError(InvalidUsage):
    pass


class SerializationError(ServerError):
    pass
