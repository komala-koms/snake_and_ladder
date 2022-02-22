import random


class Dice:
    __no_of_dice = None

    def __init__(self, __no_of_dice):
        self.__no_of_dice = __no_of_dice

    def setNumberOfDice(self, __no_of_dice):
        self.__no_of_dice = __no_of_dice

    def getNumberOfDice(self, __no_of_dice):
        return self.__no_of_dice

    def rolldice(self, __no_of_dice):
        return int((random.random() * (6 * self.__no_of_dice - 1 * self.__no_of_dice))) + 1
