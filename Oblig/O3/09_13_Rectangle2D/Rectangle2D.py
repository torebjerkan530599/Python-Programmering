class Rectangle2D:
    
    def __init__(self, x = 0, y = 0, width = 0, height = 0) -> None:
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        
        # center point of borders east,west,north,south
        self.__minX = self.__x - self.__width / 2.0
        self.__maxX = self.__x + self.__width / 2.0
        self.__minY = self.__y - self.__height / 2.0
        self.__maxY = self.__y + self.__height / 2.0
    
    def getX(self) -> float:
        return self.__x
    
    def getY(self) -> float:
        return self.__y

    def getWidth(self) -> float:
        return self.__width
    
    def getHeight(self) -> float:
        return self.__height

    def getArea(self) -> float:
        return self.__width * self.__height
    
    def getPerimeter(self) -> float:
        return self.__width * 2 + self.__height * 2
    
    def getMinX(self) -> float:
        return self.__minX
    
    def getMaxX(self) -> float:
        return self.__maxX
    
    def getMinY(self) -> float:
        return self.__minX
    
    def getMaxY(self) -> float:
        return self.__maxY
    
    def containsPoint(self, x1, y1) -> bool: 
        # Assumes positive axis downwards
        return (self.__minX < x1 < self.__maxX) and \
                    (self.__minY < y1 < self.__maxY) 
    
    #  Check if another rectangle is inside this rectangle
    def contains(self, another) -> bool:
        
        xInside = (self.__minX < another.getMinX()) and (another.getMaxX() < self.__maxX )
        yInside = (self.__minY < another.getMinY()) and (another.getMaxY() < self.__maxY )
       
        return xInside and yInside
    
    def overlaps(self, another) -> bool:     
        # if area is 0, no overlap
        if self.__minX == self.__maxX or self.__minY == self.__maxY or another.getMinX() == another.getMaxX() or another.getMinY() == another.getMaxY():
            return False
        # If one rectangle is on left side of other
        if self.__minX > another.getMaxX() or another.getMinX() > self.__maxX:
            return False
        # If one rectangle is above other
        if self.__maxY > another.getMinY() or another.getMaxY() > self.__minY:
            return False     
        return True
    
    # Check if this rectangle is inside another rectangle
    def __contains__(self, another) -> bool:
               
        xInside = (self.__minX > another.getMinX()) and (another.getMaxX() > self.__maxX)
        yInside = (self.__minY > another.getMinY()) and (another.getMaxY() > self.__maxY)
        
        return xInside and yInside    
    
    def __cmp__(self, other) -> int:
        if(self.getArea() < other.getArea()):
            return -1
        elif self.getArea() > other.getArea():
            return 1
        else:
            return 0
        
    def __lt__(self, other) -> bool:
        return self.getArea() < other.getArea()
    
    def __le__(self, other) -> bool:
        return self.getArea() <= other.getArea()
    
    def __eq__(self, other) -> bool:
        return self.getArea() == other.getArea()
    
    def __ne__(self, other) -> bool:
        return self.getArea() != other.getArea()
    
    def __gt__(self, other) -> bool:
        return self.getArea() > other.getArea()
    
    def __ge__(self, other) -> bool:
        return self.getArea() >= other.getArea()