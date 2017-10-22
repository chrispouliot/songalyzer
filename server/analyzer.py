import functools


def get_average_popularity(songs):
    num_songs = len(songs)
    if num_songs < 1:
        # If it's a list of zero songs, return zero. If it's one, return that one's popularity
        return num_songs if not num_songs else songs.pop.popularity
    return functools.reduce((lambda x, y: x + y.popularity), songs, 0) // len(songs)


def get_total_duration(songs):
    return functools.reduce((lambda x, y: x + y.duration), songs, 0)


def find_common_songs(songs1, songs2):
    # TODO: probably can do this more succinctly.. more... better
    # I'm sure you can filter on object properties
    match_list_2 = ["{}{}".format(song.title, song.artist) for song in songs2]
    return [song for song in songs1 if "{}{}".format(song.title, song.artist) in match_list_2]


# TODO: make a generic intersection func for these public funcs
def find_common_artists(songs1, songs2):
    artists1 = [song.artist for song in songs1]
    artists2 = [song.artist for song in songs2]

    return list(set(artists1).intersection(set(artists2)))
