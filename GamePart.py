import random
class Game:
    def __init__(self, player1, player2, coloda,trump):
        self.player1=player1
        self.player2=player2
        self.coloda=coloda
        self.attack=[]
        self.defend=[]
        self.trump=trump
    def choice(self):
        NOMINALS = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        if self.defend[1]==self.trump and self.attack[1]==self.trump:
            if NOMINALS.index(self.attack[0]) < NOMINALS.index(self.defend[0]):
                return True
            return False
        elif self.defend[1]==self.trump:
            return True
        elif self.attack[1]==self.trump:
            return False
        elif NOMINALS.index(self.attack[0]) < NOMINALS.index(self.defend[0]):
            return  True
        return False


