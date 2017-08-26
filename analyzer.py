import functools


def get_average_popularity(songs):
    num_songs = len(songs)
    if num_songs < 1:
        # If it's a list of zero songs, return zero. If it's one, return that one's popularity
        return num_songs if not num_songs else songs.pop.popularity
    return functools.reduce((lambda x, y: x + y.popularity), songs, 0) // len(songs)


def get_intersection(songs1, songs2):
    # TODO: probably can do this more succinctly.. more... better
    # I'm sure you can filter on object properties
    match_list_2 = ["{}{}".format(song.title, song.artist) for song in songs2]
    return [song for song in songs1 if "{}{}".format(song.title, song.artist) in match_list_2]
