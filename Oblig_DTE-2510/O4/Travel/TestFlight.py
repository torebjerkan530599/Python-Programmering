from datetime import datetime
from Flight import Flight
from Itenary import Itenary

def main():

    flights = []

    flights.append(Flight("US237",

        datetime(2014, 4, 5, 9, 35, 0),

        datetime(2014, 4, 5, 12, 55, 0)))       

    flights.append(Flight("US230",

        datetime(2014, 4, 5, 5, 5, 0),

        datetime(2014, 4, 5, 6, 15, 0)))     

    flights.append(Flight("US235",

        datetime(2014, 4, 5, 6, 55, 0),

        datetime(2014, 4, 5, 7, 45, 0)))
    


 

   

    itinerary = Itenary(flights)

    print(itinerary.getTotalTravelTime())

    print(itinerary.getTotalFlightTime())

main()