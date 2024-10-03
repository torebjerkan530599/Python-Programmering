
from GeometricObject import GeometricObject
import math

class Triangle(GeometricObject):
    
    def __init__(self, side1 = 1.0, side2 = 1.0,side3 = 1.0):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
    
    def getSide1(self) -> float:
        return self.__side1
    
    def getSide2(self) -> float:
        return self.__side2
    
    def getSide3(self) -> float:
        return self.__side3
    
    def setColor(self, color):
        super().setColor(color)
        
    def setFilled(self, filled):
        super().setFilled(filled)
        
    def getColor(self) -> str:
        return super().getColor()
    
    def isFilled(self) -> bool:
        return super().isFilled()
    
    def getArea(self) -> float:
        angle = (self.__side1 - self.__side2 - self.__side3) / -2 * self.__side2 * self.__side3 # cosinus-setningen
        area = 0.5 * math.sin(angle) * self.__side2 *  self.__side3 # areal-setningen
        return abs(area)
    
    def getPerimeter(self) -> float:
        return self.__side1 + self.__side2 + self.__side3
        
    
    def __str___(self) -> str:
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2) + " side3 = " + str(self.__side3)


if __name__ == "__main__":
    side1 = float(input('Enter side1: '))
    side2 = float(input('Enter side2: '))
    side3 = float(input('Enter side3: '))
    
    # side1 = 2.5
    # side2 = 3.1
    # side3 = 2.8 
    
    triangle = Triangle(side1,side2,side3)
    
    color = input('Enter color: ')
    triangle.setColor(color)
    #triangle.setColor('red')     
    
    filled = bool(input('Enter 1/0 for filled (1: true, 0: false): '))
    triangle.setFilled(filled)
    # triangle.setFilled(True)
    
    print(f'The area is {triangle.getArea()}')
    print(f'The perimeter is {triangle.getPerimeter()}')
    print(f'Color is  {triangle.getColor()}')
    print(f'Filled is {triangle.isFilled()}')
    print(triangle)
    