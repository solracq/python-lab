# This demonstrate polymorphism using duck typing

class Pen:
    def use(self):
        return "Writing"

class Eraser:
    def use(self):
        return "Erasing"

def perform_task(tool):
    print(tool.use())

if __name__ == "__main__":
    perform_task(Pen())
    perform_task(Eraser())