from abc import abstractmethod
from spotify import get_playlist as spotify_get_playlist


class MusicService(object):

    @abstractmethod
    def get_playlist(self, user_id, playlist_id):
        raise Exception("You must implement me!")


class SpotifyService(MusicService):
    pass
