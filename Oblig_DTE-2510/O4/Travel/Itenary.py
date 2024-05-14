class Itenary:
    def __init__(self, flights) -> None:
        self.__flights = flights
        self.__flights.sort(key=lambda  f: f.getDepartureTime()) # sort by increasing order of departureTime
        
    def getTotalFlightTime(self) : # total time in the air
        total = 0
        for f in self.__flights:
            total += f.getFlightTime()
        return total
        
    def getTotalTravelTime(self): # assembled total time
        first = self.__flights[0].getDepartureTime()
        last  = self.__flights[-1].getArrivalTime()
        return (last - first).total_seconds() / 60
