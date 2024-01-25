class TriangleError(RuntimeError):
    def __init__(self, side1, side2, side3):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
    
    def getSide1(self) -> float:
        return self.__side1
    
    def getSide2(self) -> float:
        return self.__side2
    
    def getSide3(self) -> float:
        return self.__side3
    
    def is_valid(self)-> bool:
        return self.__side1 + self.__side2 > self.__side3 and  \
                self.__side2 + self.__side3 > self.__side1 and \
                self.__side1 + self.__side3 > self.__side2
        