class Vehicle:
    def __init__(self, brand, make, model, mileage, price) -> None:
        self.__brand = brand
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
    
    @property
    def _brand(self):
        return self.__brand

    @_brand.setter
    def _brand(self, value):
        self.__brand = value
    
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
        return f'Brand: {self.__brand} Make: {self.__make} Model: {self.__model} Milage: {self.__mileage} Price: {self.__price}'