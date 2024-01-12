from Vehicle import Vehicle

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