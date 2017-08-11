from exceptions import SerializationError


class Song(object):
    title = ""
    album = ""
    artist = ""
    popularity = 0
    duration = ""

    def from_spotify(self, song_dict):
        try:
            self.title = dict['title']
            self.album = dict['album']
            self.artist = dict['artist']
            self.popularity = dict['popularity']
            self.duration = dict['duration']
        except KeyError as e:
            raise SerializationError("Failed to serialize field \"{}\"".format(e.args[0]))


class Playlist(object):
    songs = []
    owner = ""
    name = ""
    description = ""

    def from_spotify(self, playlist_dict):
        try:
            self.songs = [Song().from_spotify(song_dict) for song_dict in playlist_dict['tracks']]
            self.owner = playlist_dict['owner']
            self.name = playlist_dict['name']
            self.description = playlist_dict['description']
        except KeyError as e:
            raise SerializationError("Failed to serialize field \"{}\"".format(e.args[0]))
