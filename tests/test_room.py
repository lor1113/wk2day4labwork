import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(5,10)
        self.test_song = Song("Free Bird",500)
        self.test_guest = Guest("Alex",500,self.test_song)
        self.test_guest2 = Guest("Jhonathan",200,self.test_song)
    
    def test_room_has_occupants(self):
        self.assertEqual(self.room.occupants,[])
    
    def test_room_has_song_list(self):
        self.assertEqual(self.room.song_list,[])
    
    def test_room_has_capacity(self):
        self.assertEqual(self.room.capacity,5)
    
    def test_room_has_fee(self):
        self.assertEqual(self.room.fee,10)
    
    def test_room_has_earnings(self):
        self.assertEqual(self.room.earnings,0)
    
    def test_guest_check_in(self):
        self.room.check_in_guest(self.test_guest)
        self.assertIn(self.test_guest,self.room.occupants)
    
    def test_guest_check_out(self):
        self.room.check_in_guest(self.test_guest)
        self.room.check_out_guest(self.test_guest)
        self.assertNotIn(self.test_guest,self.room.occupants)

    def test_add_song_to_room(self):
        self.room.add_song(self.test_song)
        self.assertIn(self.test_song, self.room.song_list)

    def test_remove_song_from_room(self):
        self.room.add_song(self.test_song)
        self.room.remove_song(self.test_song)
        self.assertNotIn(self.test_song, self.room.song_list)

    def test_room_at_capacity(self):
        test_room = Room(1,10)
        test_room.check_in_guest(self.test_guest)
        test_room.check_in_guest(self.test_guest2)
        self.assertNotIn(self.test_guest2,test_room.occupants)
    
    def test_guest_pays_fee(self):
        self.room.check_in_guest(self.test_guest)
        self.assertEqual(self.test_guest.wallet,490)
    
    def test_guest_no_money(self):
        test_guest = Guest("James",0,self.test_song)
        self.room.check_in_guest(test_guest)
        self.assertNotIn(test_guest,self.room.occupants)
    
    def test_guest_fav_song(self):
        self.room.add_song(self.test_song)
        output = self.room.check_in_guest(self.test_guest)
        self.assertEqual(output,"Whoo!")
    
    def test_guest_fav_song(self):
        output = self.room.check_in_guest(self.test_guest)
        self.assertNotEqual(output,"Whoo!")
