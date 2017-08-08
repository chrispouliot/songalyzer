import requests
import os

from exceptions import AuthException, RateLimitException, ServiceException

BASE_API = "https://api.spotify.com/v1"
CLIENT_ID = os.environ.get("cliend_id")
CLIENT_SECRET = os.environ.get("cliend_secret")
# Response statuses
USER_ERROR_STATUSES = [400, 401, 403]
RATE_LIMIT_STATUS = 429
OK_STATUSES = [200, 201, 202, 204]
ERROR_STATUSES = [*USER_ERROR_STATUSES, RATE_LIMIT_STATUS, 500, 502, 503]


def _get(url):
    r = requests.get(url, auth=(CLIENT_ID, CLIENT_SECRET))
    status_code = r.status_code

    if status_code in ERROR_STATUSES:
        if status_code == RATE_LIMIT_STATUS:
            print("do some re try backoff thing first")
            raise RateLimitException("Too many requests")
        elif status_code in USER_ERROR_STATUSES:
            raise AuthException("Failed to authenticate with Spotify. Status code {}".format(status_code))
        raise ServiceException("Spotify server error. Status code {}".format(status_code))

    return r.json()


def get_playlist(user_id, playlist_id):
    url = "/users/{user_id}/playlists/{playlist_id}".format(
        user_id=user_id,
        playlist_id=playlist_id,
    )
    return _get(url)
