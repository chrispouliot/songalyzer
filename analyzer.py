import functools


def get_average_popularity(songs):
    num_songs = len(songs)
    if num_songs < 1:
        # If it's a list of zero songs, return zero. If it's one, return that one's popularity
        return num_songs if not num_songs else songs.pop.popularity
    return functools.reduce((lambda x, y: x + y.popularity), songs, 0) // len(songs)
