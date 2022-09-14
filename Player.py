from TerningSpil import TerningSpil
class Player():
    def __init__(self, name):
        self.Name = name
        self.Game = TerningSpil()

    def TakeTurn(self):
        self.Game.Play()
        return self.Game.GetFvSum() 

    def __str__(self):
        return f"player name: {self.Name}"
