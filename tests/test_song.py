import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("The Chain",200)
    
    def test_song_has_name(self):
        self.assertEqual(self.song.name,"The Chain")

    def test_song_has_runtime(self):
        self.assertEqual(self.song.runtime,200)