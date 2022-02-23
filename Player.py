class Player:
    __playerName = None
    __id = None

    def __init__(self, __playerName, __id):
        self.__playerName = __playerName
        self.__id = __id

    def setPlayerName(self, __PlayerName):
        self.__playerName = __PlayerName

    def setId(self, __id):
        self.__id = __id

    def getPlayerName(self):
        return self.__playerName

    def getId(self):
        return self.__id
