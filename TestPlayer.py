import unittest
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
class TestPlayer(unittest.TestCase):
  def setUp(self):
    self.player = Player(0,DECK)
  def test_addCard(self):
    x=len(self.player.getCards())
    self.assertEqual(self.player.addCard(DECK), x+1)
if __name__ == "__main__":
  unittest.main()