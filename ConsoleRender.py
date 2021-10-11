import os
class Render:
    def __init__(self, game):
        self.game=game
    def rendTurn(self, playerId,type):
        os.system('CLS')
        print("Размер колоды: ",len(self.game.coloda))
        print("Ход игрока ",playerId," ",type)
        print("Козырная масть: ",self.game.trump)
        print("Атака: ",self.game.attack)
        print("Защита: ",self.game.defend)
        if playerId==0:
            print(self.game.player1.cards," <= Твоя колода")
        else:
            print(self.game.player2.cards, " <= Твоя колода")
        pass
