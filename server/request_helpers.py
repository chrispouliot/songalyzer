import requests
from requests.auth import HTTPBasicAuth


class Methods(object):
    POST = 'post'
    GET = 'get'


class Auth(object):
    client_id = ''
    client_secret = ''

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def _get_request_auth(self):
        return HTTPBasicAuth(self.client_id, self.client_secret)


_method_map = {
    Methods.POST: requests.post,
    Methods.GET: requests.get,
}


def make_request(method, url, auth=None, headers=None, data=None):
    # TODO: raise error for invalid get?
    request_func = _method_map.get(method)
    if auth:
        auth = auth._get_request_auth()
    return request_func(url, auth=auth, headers=headers, data=data)
