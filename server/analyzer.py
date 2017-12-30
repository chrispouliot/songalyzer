import functools
from operator import attrgetter


def sort_songs_by_attr(songs, attr):
    return sorted(songs, key=attrgetter(attr))


def get_average_popularity(songs):
    num_songs = len(songs)
    if num_songs < 1:
        # If it's a list of zero songs, return zero. If it's one, return that one's popularity
        return num_songs if not num_songs else songs.pop.popularity
    return functools.reduce((lambda x, y: x + y.popularity), songs, 0) // len(songs)


def get_total_duration(songs):
    return functools.reduce((lambda x, y: x + y.duration), songs, 0)


def find_common_songs(songs1, songs2):
    return song_intersection(songs1, songs2, lambda song: "{}{}".format(song.title, song.artist))


def find_common_artists(songs1, songs2):
    matching_songs = song_intersection(songs1, songs2, "artist")
    return [song.artist for song in matching_songs]


def song_intersection(songs1, songs2, attribute):
    attribute_getter = attribute if callable(attribute) else lambda x: getattr(x, attribute)
    
    attrs = {attribute_getter(x) for x in songs1} & {attribute_getter(x) for x in songs2}

    return [song for song in songs1 if attribute_getter(song) in attrs]
