class Room:
    def __init__(self,capacity,fee):
        self.occupants = []
        self.song_list = []
        self.capacity = capacity
        self.fee = fee
        self.earnings = 0
    
    def check_in_guest(self,guest):
        if guest.wallet >= self.fee:
            if len(self.occupants) < self.capacity:
                self.occupants.append(guest)
                guest.remove_cash(self.fee)
                self.earnings += self.fee
                if guest.fav_song in self.song_list:
                    return "Whoo!"
    
    def check_out_guest(self,guest):
        self.occupants.remove(guest)

    def add_song(self, song):
        self.song_list.append(song)

    def remove_song(self, song):
        self.song_list.remove(song)

    


    

