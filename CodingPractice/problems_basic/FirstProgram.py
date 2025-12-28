'''
This is used to import collections classes : import collections
'''
import math
from SimpleCalculation import factorial

print("hello")
print(2+2)
a=4
b=5
print(a*b)
print(a%2)

#conditions
s="conditions"
print(s.upper())
print(1, a==b)
print(2, a<=b)
print(3, a>=b)
print(4, a==7 and b==7)
print(5, a==7 or b==7)
print(6, not(a==7 and b==7))
print(7, not a==7 and b==7)
if a<b:
    print(a,"is less than",b)

#Operations
s="operations"
print(s.upper())
print(233242*2342324)
print((5+1)/(45%2))
print(1/2,"vs",1//2) # decimal vs integer result value
print(3*2,"vs",3**2) # multiplication vs power of
print("convert a number to binary using bin()",bin(5))
print("removing the b=",format(5, 'b'))

#Appending strings and input() stirngs
s="Apending and input() strings"
print(s.upper())
name="awfg"
lastName="abc"
print(name,lastName)
name=input("What is your name?")
print(name)
age=input("What is your age") # all the data stored by input() is of 'str' type. You need to cast age as integer, int(age)
print(name,"has",age+" years old")
print(name,age)
print(type(name))
print(type(age))
print(name+age) # This is possible because name and age are of 'str' type
age2=4
print(type(age2))
print("dsafdsftos"+str(age2)) # This is not possible as '+' can ONLY concatenate str with str types. So we need to convert the int variable to str by using str()
dec=19.8
print(dec, "vs", int(dec))

print("Please, give me your name:")
name=input()
if name == "David":
    print("PASS")
else:
    print("No Passing!")
    
#Code to calculate rate and distance
print("Input a rate and distance")
rate=float(input("rate:"))
distance=float(input("distance:"))
print("time: ", rate/distance)

print(len("antidisestablishmentarianism"))

print(math.pi)
print(factorial(5))