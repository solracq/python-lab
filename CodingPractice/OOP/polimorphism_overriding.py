class Shape:
    def area(self):
        raise NotImplementedError

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.1416 * self.r * self.r


if __name__ == "__main__":
    shapes = [Square(3), Circle(5)]
    for shp in shapes:
        print(shp.area())