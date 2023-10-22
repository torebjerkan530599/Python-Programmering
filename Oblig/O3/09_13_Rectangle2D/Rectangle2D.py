class Rectangle2D:
    
    def __init__(self, x = 0, y = 0, width = 0, height = 0) -> None:
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        
    # def Rectangle2D(self, x = 0, y = 0, width = 0, height = 0):
    #     self.__x = x
    #     self.__y = y
    #     self.__width = width
    #     self.__height = height
    
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
    
    
    '''
    x1 = 9
    y1 = 1.3
    width1 = 10
    height1 = 35.3 
    '''
    def containsPoint(self, x1, y1) -> bool: 

        # testkode
        # xlessTest = self.__x - self.__width / 2.0 # expected 4 # min x
        # xmoreTest = self.__x + self.__width / 2.0 # expected 14 # max x
        # ylessTest = self.__y - self.__height / 2.0 # expected -16,35 # min y
        # ymoreTest = self.__y + self.__height / 2.0 # expected 18.95 # max y
        
        # testX = self.__x - self.__width / 2.0 < x1 < self.__x + self.__width / 2.0
        # testY = self.__y - self.__height / 2.0 < y1 < self.__y + self.__width / 2.0

        return (self.__x - self.__width / 2.0 < x1 < self.__x + self.__width / 2.0) and \
                    (self.__y - self.__height / 2.0 < y1 < self.__y + self.__width / 2.0) # swap, y increases downward onscreen, decreases upwards onscreen
    
    #  Check if another rectangle is inside this rectangle
    def contains(self, another) -> bool:
        anotherMaxX = another.getX() + another.getWidth() / 2.0
        anotherMinX = another.getX() - another.getWidth() / 2.0
        anotherMaxY = another.getY() + another.getHeight() / 2.0
        anotherMinY = another.getY() - another.getHeight() / 2.0
        
        minX = self.__x - self.__width / 2.0 # expected 4 # min x
        maxX = self.__x + self.__width / 2.0 # expected 14 # max x
        minY = self.__y - self.__height / 2.0 # expected -16,35 # min y
        maxY = self.__y + self.__height / 2.0 # expected 18.95 # max y
        
        
        xInsideTest = (minX < anotherMinX) and (anotherMaxX < maxX )
        yInsideTest = (minY < anotherMinY) and (anotherMaxY < maxY )
       
        return xInsideTest and yInsideTest
    
    def overlaps(self, another) -> bool:
        minX = self.__x - self.__width / 2.0 
        maxX = self.__x + self.__width / 2.0 
        minY = self.__y - self.__height / 2.0 
        maxY = self.__y + self.__height / 2.0 
        
        anotherMinX = another.getX() - another.getWidth() / 2.0
        anotherMaxX = another.getX() + another.getWidth() / 2.0
        anotherMinY = another.getY() - another.getHeight() / 2.0
        anotherMaxY = another.getY() + another.getHeight() / 2.0
        
        # if area is 0,no overlap
        if minX == maxX or minY == maxY or anotherMinX == anotherMaxX or anotherMinY == anotherMaxY:
            return False
        # If one rectangle is on left side of other
        if minX > anotherMaxX or anotherMinX > maxX:
            return False
        # If one rectangle is above other
        if maxY > anotherMinY or anotherMaxY > minY:
            return False
        
        return True
    
    # Check if this rectangle is inside another rectangle
    def __contains__(self, another) -> bool:
        anotherMaxX = another.getX() + another.getWidth() / 2.0
        anotherMinX = another.getX() - another.getWidth() / 2.0
        anotherMaxY = another.getY() + another.getHeight() / 2.0
        anotherMinY = another.getY() - another.getHeight() / 2.0
        
        minX = self.__x - self.__width / 2.0 # expected 4 # min x
        maxX = self.__x + self.__width / 2.0 # expected 14 # max x
        minY = self.__y - self.__height / 2.0 # expected -16,35 # min y
        maxY = self.__y + self.__height / 2.0 # expected 18.95 # max y
        
        
        xInsideTest = (minX > anotherMinX) and (anotherMaxX > maxX )
        yInsideTest = (minY > anotherMinY) and (anotherMaxY > maxY )
        
        return xInsideTest and yInsideTest      
    
    # compare two cirlces based on their areas? 
    # def __cmp__:
    # def __lt__:
    # def __le__:
    # def __eq__:
    # def __ne__:
    # def __gt__:
    # def __ge__: