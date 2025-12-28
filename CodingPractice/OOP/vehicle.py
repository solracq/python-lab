class Vehicle:
    count = 0

    def __init__(self, make, model):
        self.__make = make
        self.__model = model

    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return Vehicle._to_upper(self.__model)

    @make.setter
    def make(self, make):
        self.__make = make

    @model.setter
    def model(self, model):
        self.__model = model

    def description(self):
        return f"{self.__make} {self.__model}"

    @staticmethod
    def _to_upper(String: str):
        return String.upper()

    @classmethod
    def completed_cars(cls):
        return cls.count

    def __str__(self):
        return f"This is a car made by {self.__make} with the model {self.__model}"