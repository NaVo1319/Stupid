import random
class Player:
    def __init__(self, index, cards):
        self.index = index
        self.cards = list(map(tuple, cards))  # убедимся, что будет список кортежей
    def addCard(self,cards):
        if len(cards)==0:
            return False
        self.cards.append(cards[random.randint(0,len(cards))])
        return len(self.cards)
    def attack(self,id):
        card=self.cards[id]
        self.cards.pop(id)
        return card
        pass
    def defend(self,id):
        card = self.cards[id]
        self.cards.pop(id)
        return card
    def pickCard(self,card):
        self.cards.append(card)
        return len(self.cards)