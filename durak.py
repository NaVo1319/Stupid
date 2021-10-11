import random
from Player import Player
from GamePart import Game
from ConsoleRender import Render
import os
game=Game()
render=Render(game)
progress=0
while(True):
    if progress==0:
        if (len(game.coloda) < 24):
            render.rendTurn(progress,"Защита")
            while (progress == 0):
                step_value = int(input())-1;
                if 0 <= step_value <= len(game.player1.cards):
                    i = step_value
                    game.defend = game.player1.cards[i]
                    if game.choice():
                        game.player1.defend(i)
                        progress = 1
                    else:
                        render.No()
                elif step_value < 0:
                    game.player1.pickCard(game.attack)
                    progress = 1
            game.attack = []
            game.defend = []
        render.rendTurn(0,"Атака")
        step_value = int(input())-1;
        if 0<=step_value<=len(game.player1.cards):
            i=step_value
            game.attack=game.player1.cards[i]
            game.player1.attack(i)
            progress=1
    else:
        render.rendTurn(progress,"Защита")
        while (progress == 1):
            step_value = int(input())-1;
            if 0 <= step_value <= len(game.player2.cards):
                i = step_value
                game.defend = game.player2.cards[i]
                if game.choice():
                    game.player2.defend(i)
                    progress = 0
                else:
                    render.No()
            elif step_value<0:
                game.player2.pickCard(game.attack)
                progress =0
        if progress == 0:
            game.attack = []
            game.defend = []
            render.rendTurn(1, "Атака")
            step_value = int(input())-1;
            if 0 <= step_value <= len(game.player2.cards):
                i = step_value
                game.attack = game.player2.cards[i]
                game.player2.attack(i)
                progress = 0
    if len(game.coloda)>=2:
        game.player1.cards.append(game.coloda.pop(random.randint(0, len(game.coloda) - 1)))
        game.player2.cards.append(game.coloda.pop(random.randint(0, len(game.coloda) - 1)))
    if game.Victory()!=True:
        break



