import functools


def get_average_popularity(songs):
    if len(songs) == 1:
        return songs.pop.popularity
    return functools.reduce((lambda x, y: x + y.popularity), songs, 0) // len(songs)
