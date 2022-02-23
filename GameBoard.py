import Dice
import Player
import snake
import Ladder


class GameBoard:
    dice = None
    player = None
    snakes = None
    ladders = None
    playersCurrentPosition = {}
    boardSize = None
    nextTurn = {}

    def __init__(self, dice, nextTurn, snakes, ladders, playersCurrentPosition, boardSize):
        self.dice = dice
        self.snakes = snakes
        self.ladders = ladders
        self.playersCurrentPosition = playersCurrentPosition
        self.boardSize = boardSize
        self.nextTurn = nextTurn

    def startGame(self):
        while len(self.nextTurn) > 1:
            self.player = self.nextTurn.pop(0)
            currentPosition = self.playersCurrentPosition[self.player[0]]
            dicevalue = self.dice.rolldice(1)
            print(self.player, " got a roll of ", dicevalue)
            nextCell = currentPosition + dicevalue
            if nextCell > self.boardSize:
                self.nextTurn.append(self.player)
            elif nextCell == self.boardSize:
                print(self.player[0], " won the game")
            else:
                nextPosition = None
                b = None
                nextPosition = nextCell
                for key, value in self.snakes.items():
                    if key == nextCell:
                        nextPosition = value
                if nextPosition != nextCell:
                    print(self.player[0], " bitten by a snake at ", nextCell)
                for key, value in self.ladders.items():
                    if key == nextCell:
                        nextPosition = value
                        b = True
                if nextPosition != nextCell and b:
                    print(self.player[0], " got ladder present at ", nextCell)
                if nextPosition == self.boardSize:
                    print(self.player[0], " won the game")
                else:
                    self.playersCurrentPosition[self.player[0]] = nextPosition
                    print(self.player[0], " is at ",nextPosition)
                    self.nextTurn.append(self.player)