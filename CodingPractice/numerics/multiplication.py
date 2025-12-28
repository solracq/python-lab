from audioop import mul


def multiplication(a, b):
    mult = 0
    if (type(a) == int) and (type(b) == int):  # check that the inputs are integers
        if abs(a) != 0 or abs(b) != 0:   # Check that the inputs are absolute value and no zeros
            for i in range(abs(a)):
                mult += abs(b)
            return mult
        else:
            return 0
    else:
        print("Inputs must be integers!")

# m = multiplication(2,3)
# print(f"Multiplication result: {m}")

# m = multiplication(3,2)
# print(f"Multiplication result: {m}")

# m = multiplication(-2,-3)
# print(f"Multiplication result: {m}")

# m = multiplication(-3,-2)
# print(f"Multiplication result: {m}")

# m = multiplication(0,3)
# print(f"Multiplication result: {m}")

# m = multiplication(0,0)
# print(f"Multiplication result: {m}")

# m = multiplication(1000000,300000)
# print(f"Multiplication result: {m}")

# m = multiplication(-9000000,-900000)
# print(f"Multiplication result: {m}")

# m = multiplication('a','b')
# print(f"Multiplication result: {m}")

def parentesis_validation(s):
    array = list(s)
    op = ['{', '[', '(']
    cp = ['}', ']', ')']
    stack = []
    for i in range(len(array)):
        print(f"\n\n{i}")
        if array[i] in op:
            stack.append(array[i])
            print(f"\nSTACK OP = {stack}")
        elif array[i] in cp:
            location = cp.index(array[i])
            print(f"\nLOCATION = {location}")
            if (len(stack) > 0) and (op[location] == stack[len(stack) - 1]):
                stack.pop()
                print(f"\nSTACK POP = {stack}")
            else:
                return "UNBALANCED"
    if len(stack) == 0:
        return "BALANCED"

s = "{[()]}"
print(parentesis_validation(s))
print()
S = "{[[{}]}"
print(parentesis_validation(S))