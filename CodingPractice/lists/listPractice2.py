'''
@author: Solrac
'''
import random as rand
import time

names= ["rosita", "blanquita", "espiridion", "pluscuanperfecto", "paranguacutiminicuaro"]
print("This are the names stored in a list \n{1}\n{2}\n{4}\n{3}\n{0}\n".format(*names))

for name in names:
    if name == names[0]:
        print(name, "Que paso?")
    elif name == names[1]:
        print(name, "Que onda?")
    elif name == names[2]:
        print(name, "Quiovo?")
    elif name == names[3]:
        print(name, "Que cuentas?")
    else:
        print(name, "Como va?")

print(names)
print()

#Modifying
names[2]="chacho"
print("Modified list", names)
print()

#Adding
names= names+["elIdca"]
print("Added with +", names)
names.extend(["test"])
print("Extended", names)
names.append("ElPadrino")
print("Appended",names)
names.insert(3, "ElBuenambiente")
print("Inserted",names)
print()
numbers2=[]
for i in range(10):
    numbers2.append(rand.randint(1,9))
print(numbers2)
print()

newlist= []  #other way newlist=list()
newlist.append("object")
print(newlist,"\n")

#sorting
print(sorted(names)) # temporaly sorted, keep the original list unchanged
print(names)
print("temporary sorted in reverse",sorted(names, reverse=True))
print(names)
names.sort() # permanent sorting
print(names)
names.sort(reverse=True)
print(names)
names.reverse()
print(names)
print()

#Removing
del names[2:4]
print("Deleted from index 2 to 3", names)
names.remove("elIdca")
print("Removed idca", names)
popped_item = names.pop(4)
print("Popped out item {} the result list is: {},{},{},{},{}".format(popped_item, *names))

numbers1=[1, 1, 5, 8, 4, 6, 1, 9, 5, 7]
print(numbers1)
while 1 in numbers1:
    numbers1.remove(1)
print("After removing the 1s: ", numbers1)

list_=["a", "b", "c", "d", "e", "f"]
print("List of guests:", list_)
cant_makeit=list_.pop(4)
print("The guest that cannot make is ,", cant_makeit)
list_.insert(4, "k")
print("New List with a new invitee", list_)
for element in list_:
    print("{} you are invited to Carlitos' party".format(element))
print()    

print("found a bigger table for the invitees")
list_.insert(0, "n")
list_.insert(3, "z")
list_.append("y")
print(list_,"\n")

print("Need to drop some letters")
x=0
removed=[]
while x<=2:
    randomNo = rand.randint(0, len(list_)-1)
    if randomNo in removed:
        continue
    
    popped= list_.pop(randomNo)
    removed.append(randomNo)
    print("The removed invitee is ", popped)
    x=x+1
print("Final list", list_)
print()
list_.clear()
print("Clearing the list", list_)

pizza_flavors=["hawaian", "pesto-bacon", "goat cheese w/spinash", "ranchera"]
for pizza_flavor in pizza_flavors:
    print("I like {} pizza".format(pizza_flavor))
    if pizza_flavor == pizza_flavors[0]:
        print("Carlitos and Naomi really like", pizza_flavor)
    elif pizza_flavor == pizza_flavors[2]:
        print("Mama Yu and papa Carlos really like", pizza_flavor)
print("I really love pizza!")
print()

print(list(range(0,10)))
print(list(range(10)))
evenNumbers = list(range(0,10,2))
print(evenNumbers)
oddNumbers = list(range(1,10,2))
print(oddNumbers)
print()
squares=[]
for i in range(1,11):
    squares.append(i**2)
    print(squares[i-1]) # substracting 1 to the counter because the index in a list always go from 0 to list.length-1
print(squares)
print("maximum",max(squares))
print("minimum",min(squares))
print("sum",sum(squares))

# comprehensive lists
comprehensive_list=[i for i in range(10)]  # list format:  list_name=[i for i in range()]
print(comprehensive_list)
squares2= [i**2 for i in range(1,11)]
print(squares2)

list_ = [i for i in range(1,21)]
print(list_)
print()

start_time = time.time()
million_list = [i for i in range(1,1001)]
print(million_list)
print(min(million_list))
print(max(million_list))
print(sum(million_list))
print("Elapsed time:", time.time()-start_time)
print(time.asctime(),"\n")

list_a=[i for i in range(1,21,2)]
print(list_a,"\n")

multiple_3 = [i for i in range(3,30,3)]
print(multiple_3,"\n")

cubes=list()
for i in range(1,11):
    cubes.append(i**3)
    print(cubes[i-1])
print(cubes,"\n")

cubes2= [i**3 for i in range(1,11)]
print(cubes2,"\n")

# slicing lists
subsets = ["a", "b", "c", "d", "e", "f"]
for subset in subsets[-5:-1]:
    print(subset)
    
#copying
print("subsets=",subsets)
subsets.append('g')
print(subsets,"\n")
subsets_ = subsets[:]
print("subsets_=",subsets_)
subsets_.append('h')
print(subsets_,"\n")
subsets__=subsets_[-7:-2]
print(subsets__,"\n")

carlitos_pizza_flav = pizza_flavors[:]
print(carlitos_pizza_flav,"\n")
carlitos_pizza_flav.append("pepperoni")
print("carlitos",carlitos_pizza_flav,"\n")
print("papa", pizza_flavors,"\n")
for flavor_papa in pizza_flavors[1:4]:
    print("flavorPapa",flavor_papa)
print()
for flavor_carlitos in carlitos_pizza_flav[:2]:
    print("flavorCarlitos",flavor_carlitos)
print()

