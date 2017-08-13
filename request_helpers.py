import requests

from exceptions import AuthError, ServiceError


class Methods(object):
    POST = 'post'
    GET = 'get'


_method_request_map = {
    Methods.POST: requests.post,
    Methods.GET: requests.get,
}


def raise_for_status(status_code, error_statuses, user_error_statuses):
    if status_code in error_statuses:
        if status_code in user_error_statuses:
            raise AuthError("Failed to authenticate with Spotify. Status code {}".format(status_code))
        raise ServiceError("Spotify server error. Status code {}".format(status_code))


def make_request(method, url, headers=None, data=None):
    pass
