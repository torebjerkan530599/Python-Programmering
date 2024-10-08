class Vehicle:
    def __init__(self, make, model, mileage, price, licence_plate) -> None:
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
        self.__licence_plate = licence_plate
        self.__tickets = {}
    
    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, value):
        self.__make = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def _mileage(self, value):
        self.__mileage = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def _price(self, value):
        self.__price = value
        
    @property
    def licence_plate(self):
        return self.__licence_plate

    @licence_plate.setter
    def _licence_plate(self, value):
        self.__licence_plate = value

    @property
    def tickets(self):
        return self.__tickets

    @tickets.setter
    def tickets(self, ticket):
        self.__tickets[ticket.date] = (ticket.licence_plate,ticket.speed,ticket.speed_limit)

    def __str__(self) -> str:
        return f'Make: {self.__make} Model: {self.__model} Milage: {self.__mileage} Price: {self.__price} Registration: {self.__licence_plate}'

class Car(Vehicle):
    def __init__(self, make, model, mileage, price, doors, licence_plate):
        super().__init__(make, model, mileage, price,licence_plate)
        self.__doors = doors

    @property
    def doors(self):
        return self.__doors

    @doors.setter
    def doors(self, value):
        self.__doors = value

        
    def __str__(self):
        return  f'{super().__str__()} Doors: {self.__doors}'

class Suv(Vehicle):
    def __init__(self, make, model, mileage, price, pass_cap, licence_plate):
        super().__init__(make, model, mileage, price, licence_plate)
        self.__pass_cap = pass_cap

    @property
    def pass_cap(self):
        return self.__pass_cap

    @pass_cap.setter
    def pass_cap(self, value):
        self.__pass_cap = value

    def __str__(self) -> str:
        return f'{super().__str__()} Number of passengers: {self.__pass_cap}'
    
class Truck(Vehicle):
    def __init__(self, make, model, mileage, price, drive_type, licence_plate):
        super().__init__(make, model, mileage, price, licence_plate)
        self.__drive_type = drive_type

    @property
    def drive_type(self):
        return self.__drive_type

    @drive_type.setter
    def drive_type(self, value):
        self.__drive_type = value

    def __str__(self) -> str:
        return super().__str__() + " Drivetype: " +  self.__drive_type

class SpeedTicket():
    def __init__(self, license_plate, date, speed, speed_limit):
        self.__license_plate = license_plate
        self.__date = date
        self.__speed = speed
        self.__speed_limit = speed_limit
    
    @property
    def licence_plate(self):
        return self.__license_plate
    
    @property
    def date(self):
        return self.__date

    @property
    def speed(self):
        return self.__speed
    
    @property
    def speed_limit(self):
        return self.__speed_limit
    
    
    def __str__(self):
        return f'\n***Speeding Ticket***\nLicence plate: {self.__license_plate}, Date: {self.__date}, Speed: {self.__speed}, Speed Limit: {self.__speed_limit}'
    
    def __repr__(self): # because Vehicle.tickets retuns a list of objects of type SpeedTicket()
        return self.__str__()
    
    
    