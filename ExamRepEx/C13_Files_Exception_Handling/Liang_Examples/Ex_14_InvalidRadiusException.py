class InvalidRadiusException(RuntimeError):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius
        
    def getRadius(self):
        return self.__radius # tell the caller which radius caused the exception
