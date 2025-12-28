from calculator_interface import CalculatorInterface

class CalculatorScientific(CalculatorInterface):

    def __init__(self, a: int = 0, b: int = 0):
        self.a = a
        self.b = b

    def addition(self, a: int, b:int) -> int:
        if a > 0:
            self.a = a
        if b > 0:
            self.b = b
        return a + b

    def substraction(self, a: int, b: int) -> int:
        if a > 0:
            self.a = a
        if b > 0:
            self.b = b
        return a - b

    def multiplication(self, a:int, b:int) -> int:
        self.a = a
        self.b = b
        return a * b

    def division(self, a:int, b:int) -> int:
        self.a = a
        if a > b and b > 0:
            self.b = b
        return a / b

    @property
    def calculator_type(self):
        return "Scientific"


if __name__ == "__main__":
    calc = CalculatorScientific()
    print(calc.intro())
    print(calc.calculator_type)
    print(calc.addition(5, 3))
    print(calc.substraction(8, 3))
    print(calc.multiplication(2, 3))
    print(calc.division(6, 2))