from Vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, make, model, mileage, price, drive_type):
        super().__init__(make, model, mileage, price)
        self.__drive_type = drive_type

    @property
    def _drive_type(self):
        return self.__drive_type

    @_drive_type.setter
    def _drive_type(self, value):
        self.__drive_type = value

    def __str__(self) -> str:
        return super().__str__() + " Drivetype: " +  self.__drive_type