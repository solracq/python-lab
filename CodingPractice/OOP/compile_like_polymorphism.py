class Calculator:
    def multiply(self, a: int=1, b: int=1, *args) -> int:
        res = a * b
        for num in args:
            res *= num
        return res

if __name__ == "__main__":
    calc = Calculator()
    print(calc.multiply())
    print(calc.multiply(5))
    print(calc.multiply(3, 9))
    print(calc.multiply(5, 7, 8))
    print(calc.multiply(9, 7, 5, 2))