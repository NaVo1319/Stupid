import random
from Player import Player
# масти
SPADES = '♠'
HEARTS = '♥'
DIAMS = '♦'
CLUBS = '♣'
# достоинтсва карт
NOMINALS = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# поиск индекса по достоинству
NAME_TO_VALUE = {n: i for i, n in enumerate(NOMINALS)}
# карт в руке при раздаче
CARDS_IN_HAND_MAX = 6
N_PLAYERS = 2
# эталонная колода (каждая масть по каждому номиналу) - 36 карт
DECK = [(nom, suit) for nom in NOMINALS for suit in [SPADES, HEARTS, DIAMS, CLUBS]]
class Game:
    def __init__(self):
        # Раздача карт
        self.coloda = random.shuffle(list(DECK))
        # Первому игроку
        cp1 = [self.coloda.pop(random.randint(0, len(self.coloda) - 1))]
        for i in range(5):
            cp1.append(self.coloda.pop(random.randint(0, len(self.coloda) - 1)))
        self.player1 = Player(1, cp1)
        # Второму игроку
        cp2 = [self.coloda.pop(random.randint(0, len(self.coloda) - 1))]
        for i in range(5):
            cp2.append(self.coloda.pop(random.randint(0, len(self.coloda) - 1)))
        self.player2=player2 = Player(1, cp2)
        self.attack=[]
        self.defend=[]
        self.trump=[SPADES, HEARTS, DIAMS, CLUBS][random.randint(0,3)]
        self.VictoryPlayer='Нет'
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
    def Victory(self):
        if len(self.coloda) == 0:
            if len(self.player1.cards) == 0 and  len(self.player2.cards) == 0:
                self.VictoryPlayer = 'Нечья'
                x = input()
                return False
            if len(self.player1.cards) == 0:
                self.VictoryPlayer='Игрок 1 победил'
                x = input()
                return False
            if len(self.player2.cards) == 0:
                self.VictoryPlayer = 'Игрок 2 победил'
                x = input()
                return False
        return True


