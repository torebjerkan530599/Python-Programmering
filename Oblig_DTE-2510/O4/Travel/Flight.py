from datetime import datetime

class Flight:
    
    def __init__(self, flightNumber, departureTime , arrivalTime) -> None:
        self.__departureTime = departureTime
        self.__arrivalTime = arrivalTime
        self.__flightNumber = flightNumber

    def getFlightNumber(self):
        return self.__flightNumber

    def getDepartureTime(self):
        return self.__departureTime
    
    def setDepartureTime(self,departureTime):
        self.departureTime = departureTime

    def getArrivalTime(self):
        return self.__arrivalTime
    
    def setArrivalTime(self,arrivalTime):
        self.arrivalTime = arrivalTime

    def getFlightTime(self):
        return (self.__arrivalTime - self.__departureTime).total_seconds() / 60
