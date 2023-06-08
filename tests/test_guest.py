import unittest
from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.test_song = Song("Let It Go",300)
        self.guest = Guest("Thomas",100,self.test_song)
    
    def test_guest_has_name(self):
        self.assertEqual(self.guest.name,"Thomas")
    
    def test_guest_has_wallet(self):
        self.assertEqual(self.guest.wallet,100)
    
    def test_guest_has_fav_song(self):
        self.assertEqual(self.guest.fav_song,self.test_song)
    
    def test_guest_has_tab(self):
        self.assertEqual(self.guest.tab,[])
    
    def test_guest_remove_cash(self):
        self.guest.remove_cash(50)
        self.assertEqual(self.guest.wallet, 50)

    def test_guest_add_tab(self):
        self.guest.add_to_tab("cake",50)
        self.assertEqual(self.guest.tab,[["cake",50]])
    