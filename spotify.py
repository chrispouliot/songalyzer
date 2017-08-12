import datetime
import requests
import os
from requests.auth import HTTPBasicAuth

from exceptions import AuthError, ServiceError
from serializers import Playlist

BASE_URL = "https://api.spotify.com/v1"
AUTHORIZE_URL = "https://accounts.spotify.com/api/token"

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
GRANTED_TOKEN = ""
TOKEN_EXPIRY_DATE = datetime.datetime.now()

# Response statuses
USER_ERROR_STATUSES = [400, 401, 403]
RATE_LIMIT_STATUS = 429
OK_STATUSES = [200, 201, 202, 204]
ERROR_STATUSES = [*USER_ERROR_STATUSES, RATE_LIMIT_STATUS, 500, 502, 503]


def _raise_for_status(status_code):
    if status_code in ERROR_STATUSES:
        if status_code in USER_ERROR_STATUSES:
            raise AuthError("Failed to authenticate with Spotify. Status code {}".format(status_code))
        raise ServiceError("Spotify server error. Status code {}".format(status_code))


def _authenticate(re_auth=False):
    # TODO: why use globals instead of a class
    global TOKEN_EXPIRY_DATE, GRANTED_TOKEN
    token_valid = TOKEN_EXPIRY_DATE > datetime.datetime.now()
    
    if token_valid and not re_auth:
        return GRANTED_TOKEN

    data = {
        "grant_type": "client_credentials"
    }

    r = requests.post(
        AUTHORIZE_URL,
        auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
        data=data
    )

    _raise_for_status(r.status_code)

    body = r.json()
    expiry = body.get("expires_in")
    token = body.get("access_token")

    if not expiry or not token:
        raise AuthError(
            "Failed to authenticate with Spotify. Invalid tokens returned. Status code {}".format(
                r.status_code
            )
        )
    
    TOKEN_EXPIRY_DATE = datetime.datetime.now() + datetime.timedelta(seconds=expiry)
    GRANTED_TOKEN = token
    return token


def _get(url):
    token = _authenticate()
    headers = {"Authorization": "Bearer {token}".format(token=token)}

    r = requests.get(url, headers=headers)
    _raise_for_status(r.status_code)

    return r.json()


def get_playlist(user_id, playlist_id):
    url = "{base}/users/{user_id}/playlists/{playlist_id}".format(
        base=BASE_URL,
        user_id=user_id,
        playlist_id=playlist_id,
    )

    results = _get(url)
    next_results_url = results['tracks']['next']

    # Get all tracks. Spotify paginates long results
    while next_results_url:
        paginated_results = _get(next_results_url)
        next_results_url = paginated_results['next']

        results['tracks']['items'] += paginated_results['items']

    return Playlist.from_spotify(results)
