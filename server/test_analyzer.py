import unittest
from uuid import uuid4

from .serializers import Song
from .analyzer import song_intersection, find_common_songs, find_common_artists


class SongIntersectionTests(unittest.TestCase):
    common1, common2, songs1, songs2 = [None, None, [], []]

    def setUp(self):
        _init_sample_songs(self)

    def test_basic_case_with_simple_attribute(self):
        expected = {self.common1, self.common2}

        common_songs = song_intersection(self.songs1, self.songs2, "artist")

        self.assertEqual(expected, set(common_songs))

    def test_basic_case_with_computed_attribute(self):
        attribute_getter = lambda x: "{}{}".format(x.title, x.artist)
        expected = {self.common1, self.common2}

        common_songs = song_intersection(self.songs1, self.songs2, attribute_getter)

        self.assertEqual(expected, set(common_songs))

class FindCommonSongs(unittest.TestCase):
    common1, common2, songs1, songs2 = [None, None, [], []]

    def setUp(self):
        _init_sample_songs(self)

    def test_basic_case(self):
        expected = {self.common1, self.common2}

        matches = find_common_songs(self.songs1, self.songs2)

        self.assertEqual(expected, set(matches))

    def test_no_common_songs(self):
        self.songs1 = [_random_song() for _ in range(10)]
        self.songs2 = [_random_song() for _ in range(10)]

        matches = find_common_songs(self.songs1, self.songs2)

        self.assertEqual([], matches)


class FindCommonArtists(unittest.TestCase):
    common1, common2, songs1, songs2 = [None, None, [], []]

    def setUp(self):
        _init_sample_songs(self)

    def test_basic_case(self):
        expected = {self.common1.artist, self.common2.artist}

        matches = find_common_artists(self.songs1, self.songs2)

        self.assertEqual(expected, set(matches))

    def test_no_common_songs(self):
        self.songs1 = [_random_song() for _ in range(10)]
        self.songs2 = [_random_song() for _ in range(10)]

        matches = find_common_artists(self.songs1, self.songs2)

        self.assertEqual([], matches)

        
def _init_sample_songs(self):
    # set up two collections of songs with two songs in common
    self.common1 = Song("titlecommon1", "albulmcommon1",
                        "artistcommon1", "popularitycommon1", 100)
    self.common2 = Song("titlecommon2", "albulmcommon2",
                        "artistcommon2", "popularitycommon2", 150)

    self.songs1 = [_random_song() for _ in range(10)]
    self.songs2 = [_random_song() for _ in range(10)]
    self.songs1[3] = self.common1
    self.songs1[0] = self.common2
    self.songs2[-1] = self.common1
    self.songs2[-3] = self.common2

def _random_song():
    # generate a song with random data
    return Song(str(uuid4()), str(uuid4()), str(uuid4()), str(uuid4()), str(uuid4()))
