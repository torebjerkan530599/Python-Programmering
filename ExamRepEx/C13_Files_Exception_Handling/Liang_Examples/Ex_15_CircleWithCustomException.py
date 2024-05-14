from Ex_14_InvalidRadiusException import InvalidRadiusException 
import math

class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled
  
    def __str__(self):
        return "color: " + self.__color + \
            " and filled: " + str(self.__filled)

class Circle(GeometricObject):
    def __init__(self, radius):
        super().__init__()
        self.setRadius(radius)

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        if radius >= 0:
            self.__radius = radius
        else:
            raise InvalidRadiusException(radius)

    def getArea(self):
        return self.__radius * self.__radius * math.pi
  
    def getDiameter(self):
        return 2 * self.__radius
  
    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def printCircle(self):
        print(self.__str__(), "radius:", self.__radius)
