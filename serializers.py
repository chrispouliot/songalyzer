from exceptions import SerializationError


class Song(object):
    title = ""
    album = ""
    artist = ""
    popularity = 0
    duration = ""

    def from_spotify(self, song_dict):
        try:
            artists = [artist['name'] for artist in song_dict['artists']]
            self.artist = ", ".join(artists)

            self.title = song_dict['name']
            self.album = song_dict['album']
            self.popularity = song_dict['popularity']

            duration_ms = song_dict['duration_ms']
            self.duration = (duration_ms / (1000 * 60)) % 60
            return self
        except KeyError as e:
            raise SerializationError("Failed to serialize field \"{}\"".format(e.args[0]))


class Playlist(object):
    songs = []
    owner = ""
    name = ""
    description = ""

    def from_spotify(self, playlist_dict):
        try:
            self.songs = [Song().from_spotify(song_dict['track']) for song_dict in playlist_dict['tracks']['items']]
            self.owner = playlist_dict['owner']
            self.name = playlist_dict['name']
            self.description = playlist_dict['description']
            return self
        except KeyError as e:
            raise SerializationError("Failed to serialize field \"{}\"".format(e.args[0]))
