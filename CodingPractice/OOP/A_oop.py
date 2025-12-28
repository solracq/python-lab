class Pen:
    def use(self):
        return "writting"

class Eraser:
    def use(self):
        return "erasing"

def perform_op(operation):
    print(operation.use())

perform_op(Pen())
perform_op(Eraser())