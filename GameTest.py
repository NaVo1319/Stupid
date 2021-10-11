import unittest
import random
from GamePart import Game
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
class TestGame(unittest.TestCase):
  def setUp(self):
      Coloda = list(DECK)
      # Первому игроку
      cp1 = [Coloda.pop(random.randint(0, len(Coloda) - 1))]
      for i in range(5):
          cp1.append(Coloda.pop(random.randint(0, len(Coloda) - 1)))
      player1 = Player(1, cp1)
      # Второму игроку
      cp2 = [Coloda.pop(random.randint(0, len(Coloda) - 1))]
      for i in range(5):
          cp2.append(Coloda.pop(random.randint(0, len(Coloda) - 1)))
      player2 = Player(1, cp2)
      self.game = Game(player1, player2, Coloda, '♣')

  def test_choice(self):
    self.game.attack=(NOMINALS[0],CLUBS)
    self.game.defend = (NOMINALS[1],CLUBS)
    self.assertEqual(self.game.choice(), True)
    self.game.attack = (NOMINALS[1], CLUBS)
    self.game.defend = (NOMINALS[0], CLUBS)
    self.assertEqual(self.game.choice(), False)
    self.game.attack = (NOMINALS[5], HEARTS)
    self.game.defend = (NOMINALS[1], CLUBS)
    self.assertEqual(self.game.choice(), True)
if __name__ == "__main__":
  unittest.main()