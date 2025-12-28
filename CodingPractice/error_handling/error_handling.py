import pdb
# to run debug mode
# pdb.run('function')
# python -m pdb myscript.py

numpairs = [(5,1), (1,5), (5,0), (0,5)]
total = 0

for x, y in numpairs:
    try:
        quotient = x / y
    except Exception as e:
        print(f"uh-oh, when y = {y} , {e}")
    else:
        total += quotient
print(total)

try:
    x = 5
    y = 37
    z = x + y
    print(f"z is = {z}")
except TypeError as e:
    print("Caught exception: ", e)
finally:
    print("Don't care whether we had an exception")
print()

try:
    x = 5
    y = "cheese"
    x = x + y
    print("Bottom of try")
except TypeError as e:
    print("Caught exception: ", e)
finally:
    print("Don't care whether we had an exception")
print()