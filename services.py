from abc import ABC, abstractmethod
from exceptions import InvalidQueryException
from spotify import get_playlist as spotify_get_playlist


class MusicService(ABC):

    def __init__(playlist_query):
        if "spotify" in playlist_query:
            return SpotifyService()

        # Sanity check, should never get here (famous last words)
        raise InvalidQueryException("Could not read playlist query")

    @abstractmethod
    def get_playlist(self, user_id, playlist_id):
        raise NotImplementedError("You must implement me!")


class SpotifyService(MusicService):

    def get_playlist(self, user_id, playlist_id):
        return spotify_get_playlist(user_id, playlist_id)
