from abc import ABC, abstractmethod
from .exceptions import InvalidQueryError
from .spotify import get_playlist as spotify_get_playlist


def get_music_service(playlist_query):
    if "spotify" in playlist_query:
            return SpotifyService(playlist_query)

    if "soundcloud" in playlist_query:
        return SoundCloudService(playlist_query)

    raise InvalidQueryError("Could not read playlist query")


class MusicService(ABC):

    @abstractmethod
    def __init__(self, playlist_query):
        raise NotImplementedError("You must implement me!")

    @abstractmethod
    def get_playlist(self):
        raise NotImplementedError("You must implement me!")


class SpotifyService(MusicService):

    user_id = ""
    playlist_id = ""

    def __init__(self, playlist_query):
        # TODO: omg NO
        query_parts = playlist_query.split("/")
        self.playlist_id = query_parts[-1]
        self.user_id = query_parts[-3]

    def get_playlist(self):
        return spotify_get_playlist(self.user_id, self.playlist_id)


# TODO: SoundCloud API currently unavailable
class SoundCloudService(MusicService):
    def __init__(self, playlist_query):
        pass

    def get_playlist(self):
        pass
