import random
class Player:
    def __init__(self, index, cards):
        self.index = index
        self.cards = list(map(tuple, cards))  # убедимся, что будет список кортежей
    def getCards(self):
        return self.cards
    def addCard(self,cards):
        if len(cards)==0:
            return false
        self.cards.append(cards[random.randint(0,len(cards))])
        return len(self.cards)
    def attack(self,id):
        pass
    def defend(self,id):
        pass
    def pickCard(self,card):
        pass