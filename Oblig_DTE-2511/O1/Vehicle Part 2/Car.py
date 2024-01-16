from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, make, model, mileage, price, doors):
        super().__init__(make, model, mileage, price)
        self.__doors = doors

    @property
    def _doors(self):
        return self.__doors

    @_doors.setter
    def _doors(self, value):
        self.__doors = value

        
    def __str__(self):
        return  f'{super().__str__()} Doors: {self.__doors}'
    
