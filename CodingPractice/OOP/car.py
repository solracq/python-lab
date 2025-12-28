from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.__doors = doors

    @property
    def doors(self):
        return self.__doors

    @doors.setter
    def doors(self, doors):
        self.__doors = doors

    def description(self):
        return f"{super().description()} with {self.__doors}"

    def __str__(self):
        return f"This is a car made by {self.make} with the model {self.model} and {self.__doors} doors"


if __name__ == "__main__":
    car = Car("Toyota", "Corolla", 4)
    print(car)
    print(car.description())