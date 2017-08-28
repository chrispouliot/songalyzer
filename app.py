from flask import Flask

from server.services import get_music_service
from server.analyzer import get_average_popularity, find_common_artists, find_common_songs


app = Flask(__name__)


def main(playlist_query1, playlist_query2):
    # just manual testing
    service1, service2 = get_music_service(playlist_query1), get_music_service(playlist_query2)
    playlist1, playlist2 = service1.get_playlist(), service2.get_playlist()

    print("pl1: average pop: {}".format(get_average_popularity(playlist1.songs)))
    print("pl2: average pop: {}".format(get_average_popularity(playlist2.songs)))

    song_matches = find_common_songs(playlist1.songs, playlist2.songs)
    if song_matches:
        print("\nFound {} matching songs:\n".format(len(song_matches)))
        for matched_song in song_matches:
            print("{} - {}".format(matched_song.title, matched_song.artist))

    artist_matches = find_common_artists(playlist1.songs, playlist2.songs)
    if artist_matches:
        print("\nFound {} matching artists:\n".format(len(artist_matches)))
        for matched_artist in artist_matches:
            print(matched_artist)


@app.route('/')
@app.route('/index')
def index():
    return "what what"
