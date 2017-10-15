import datetime
import os
import logging

from .exceptions import ServiceError
from .request_helpers import Auth, make_request, Methods
from .serializers import Playlist

BASE_URL = "https://api.spotify.com/v1"
AUTHORIZE_URL = "https://accounts.spotify.com/api/token"

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
GRANTED_TOKEN = ""
TOKEN_EXPIRY_DATE = datetime.datetime.now()

# TODO: I think the error-handling in this file could be revisited


def _authenticate(re_auth=False):
    global TOKEN_EXPIRY_DATE, GRANTED_TOKEN
    token_valid = TOKEN_EXPIRY_DATE > datetime.datetime.now()
    
    if token_valid and not re_auth:
        return GRANTED_TOKEN

    data = {
        "grant_type": "client_credentials"
    }

    auth = Auth(CLIENT_ID, CLIENT_SECRET)
    r = make_request(Methods.POST, AUTHORIZE_URL, auth=auth, data=data)

    if r.status_code >= 400 and r.status_code < 500:
        logging.warning("We did a bad request to spotify! status: %s, data: %s", r.status_code, data)
        raise ServiceError("Unable to fulfill your request")
    elif r.status_code >= 500:
        logging.warning("Spotify replied with a status: %s for data: %s", r.status_code, data)
        # TODO: Re try!
        raise ServiceError("Unable to fulfill your request")

    body = r.json()
    expiry = body.get("expires_in")
    token = body.get("access_token")

    if not expiry or not token:
        logging.warning(
            "Failed to authenticate with Spotify. Invalid tokens returned. Status code %s",
            r.status_code
        )
        raise ServiceError("Unable to fulfill your request")
    
    TOKEN_EXPIRY_DATE = datetime.datetime.now() + datetime.timedelta(seconds=expiry)
    GRANTED_TOKEN = token
    return token


def _get(url):
    token = _authenticate()
    headers = {"Authorization": "Bearer {token}".format(token=token)}

    r = make_request(Methods.GET, url, headers=headers)

    if r.status_code >= 400 and r.status_code < 500:
        logging.warning("We did a bad auth request to spotify! status: %s", r.status_code)
        raise ServiceError("Unable to fulfill your request")
    elif r.status_code >= 500:
        logging.warning("Spotify replied with a status: %s", r.status_code)
        # TODO: Re try!
        raise ServiceError("Unable to fulfill your request")

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
