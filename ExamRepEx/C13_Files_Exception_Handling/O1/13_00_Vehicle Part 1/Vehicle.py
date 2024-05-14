class Vehicle:
    def __init__(self, make, model, mileage, price) -> None:
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
        
    @property
    def _make(self):
        return self.__make

    @_make.setter
    def _make(self, value):
        self.__make = value

    @property
    def _model(self):
        return self.__model

    @_model.setter
    def _model(self, value):
        self.__model = value

    @property
    def _mileage(self):
        return self.__mileage

    @_mileage.setter
    def _mileage(self, value):
        self.__mileage = value

    @property
    def _price(self):
        return self.__price

    @_price.setter
    def _price(self, value):
        self.__price = value

    def __str__(self) -> str:
        return f'Make: {self.__make} Model: {self.__model} Milage: {self.__mileage} Price: {self.__price}'

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

class Suv(Vehicle):
    def __init__(self, make, model, mileage, price, pass_cap):
        super().__init__(make, model, mileage, price)
        self.__pass_cap = pass_cap

    @property
    def _pass_cap(self):
        return self.__pass_cap

    @_pass_cap.setter
    def _pass_cap(self, value):
        self.__pass_cap = value

    def __str__(self) -> str:
        return f'{super().__str__()} Number of passengers: {self.__pass_cap}'
    
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