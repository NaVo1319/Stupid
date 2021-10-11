import random
from Player import Player
from GamePart import Game
import os
game=Game()
progress=0
while(True):
    os.system('CLS')
    print("Атака ",game.attack)
    print(len(game.coloda))
    if progress==0:
        print(game.player1.cards)
        if (len(game.coloda) < 24):
            while (progress == 0):
                print('Ход игрока 1 - Защита')
                step_value = int(input())-1;
                if 0 <= step_value <= len(game.player1.cards):
                    i = step_value
                    game.defend = game.player1.cards[i]
                    if game.choice():
                        game.player1.defend(i)
                        print('Защита: ' + game.defend[0] + game.defend[1])
                        progress = 1
                    else:
                        print('Это невозможно')
                elif step_value < 0:
                    game.player1.pickCard(game.attack)
                    progress = 1
        print('Ход игрока 1 - Атака')
        step_value = int(input())-1;
        if 0<=step_value<=len(game.player1.cards):
            i=step_value
            game.attack=game.player1.cards[i]
            game.player1.attack(i)
            print('Атака: '+game.attack[0]+game.attack[1])
            progress=1
    else:
        print(game.player2.cards)
        print('Ход игрока 2')
        while (progress == 1):
            step_value = int(input())-1;
            if 0 <= step_value <= len(game.player2.cards):
                i = step_value
                game.defend = game.player2.cards[i]
                if game.choice():
                    game.player2.defend(i)
                    print('Защита: ' + game.defend[0] + game.defend[1])
                    progress = 0
                else:
                    print('Это невозможно')
            elif step_value<0:
                game.player2.pickCard(game.attack)
                progress =0
        print(game.player1.cards)
        print(game.player2.cards)
        if progress == 0:
            print('Ход игрока 2')
            step_value = int(input())-1;
            if 0 <= step_value <= len(game.player2.cards):
                i = step_value
                game.attack = game.player2.cards[i]
                game.player2.attack(i)
                print('Атака: ' + game.attack[0] + game.attack[1])
                progress = 0
    if len(game.coloda)>=2:
        game.player1.cards.append(game.coloda.pop(random.randint(0, len(game.coloda) - 1)))
        game.player2.cards.append(game.coloda.pop(random.randint(0, len(game.coloda) - 1)))
    if game.Victory()!=True:
        break



