from datetime import datetime

class Flight:
    
    def __init__(self, flightNumber, departureTime , arrivalTime) -> None:
        self.__departureTime = departureTime
        self.__arrivalTime = arrivalTime
        self.__flightNumber = flightNumber
        #self.departureTime = departureTime
        #self.arrivalTime = arrivalTime

    def getFlightNumber(self):
        return self.__flightNumber

    def getDepartureTime(self):
        return self.__departureTime

    def getArrivalTime(self):
        return self.__arrivalTime

    def getFlightTime(self):
        return (self.__arrivalTime - self.__departureTime).total_seconds() / 60
