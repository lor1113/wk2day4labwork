class Guest:
    def __init__(self,name,wallet,fav_song = None):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song
        self.tab = []
    
    def remove_cash(self,amount):
        self.wallet -= amount

    def add_to_tab(self,product,amount):
        self.tab.append([product,amount])
    
    def print_receipt(self):
        for entry in self.tab:
            print(entry[0],entry[1])

    def pay_tab(self):
        total = 0
        for entry in self.tab:
            total += entry[1]
        if self.wallet >= total:
           self.remove_cash(total)
           self.print_receipt()
           self.tab = []

