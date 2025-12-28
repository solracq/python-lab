from abc import ABC, abstractmethod

class CalculatorInterface(ABC):
    @abstractmethod
    def addition(self, a: int, b:int) -> int:
        pass

    @abstractmethod
    def substraction(self, a: int, b: int) -> int:
        pass

    @abstractmethod
    def multiplication(self, a:int, b:int) -> int:
        pass

    @abstractmethod
    def division(self, a:int, b:int) -> int:
        pass

    @property
    @abstractmethod
    def calculator_type(self):
        pass

    def intro(self):
        return "This is a Calculator"