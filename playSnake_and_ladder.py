from Dice import Dice
from Player import Player
from snake import Snake
from Ladder import Ladder
from GameBoard import GameBoard


class playSnake_and_ladder:
    dice = Dice(1)
    player1 = Player("Komala", 1)
    player2 = Player("Harsha", 2)
    allPlayers = list()
    allPlayers.append([player1.getPlayerName(), player1.getId()])
    allPlayers.append([player2.getPlayerName(), player2.getId()])
    snake1 = Snake(10, 2)
    snake2 = Snake(99, 12)
    snakes = {}
    snakes[snake1.getStartPoint()] = snake1.getEndPoint()
    snakes[snake2.getStartPoint()] = snake2.getEndPoint()
    ladder1 = Ladder(5, 25)
    ladder2 = Ladder(40, 89)
    ladders = dict()
    ladders[ladder1.getStartPoint()] = ladder1.getEndPoint()
    ladders[ladder2.getStartPoint()] = ladder2.getEndPoint()
    playersCurrentPosition = dict()
    playersCurrentPosition["Komala"] = 0
    playersCurrentPosition["Harsha"] = 0
    gb = GameBoard(dice, allPlayers, snakes, ladders, playersCurrentPosition, 100)
    gb.startGame()