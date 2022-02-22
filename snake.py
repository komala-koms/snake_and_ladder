class Snake:
    __startPoint = None
    __endPoint = None

    def Snake(self, __startPoint, __endPoint):
        self.__startPoint = __startPoint
        self.__endPoint = __endPoint

    def getStartPoint(self):
        return self.__startPoint

    def getEndPoint(self):
        return self.__endPoint

    def setStartPoint(self, __startPoint):
        self.__startPoint = __startPoint

    def setEndPoint(self, __endPoint):
        self.__endPoint = __endPoint
