class AuthError(Exception):
    pass


class RateLimitError(Exception):
    pass


class ServiceError(Exception):
    pass


class InvalidQueryError(Exception):
    pass


class SerializationError(Exception):
    pass
