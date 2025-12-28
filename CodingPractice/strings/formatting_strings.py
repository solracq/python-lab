'''
@author: Solrac
'''
name="Conan"
place="Aquilonia"
hobbie="barbarian"
timeago=1000
print("The {} hero of the {} Age ({}BC) is: {}".format(hobbie, place, timeago, name))

numbers= 2, 4, 6, 8, 9, 0, 4, 6, 3, 7, 1
print("This are the numbers: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(*numbers))
print("This are the numbers using its index: {10}, {9}, {8}, {7}, {6}, {5}, {4}, {3}, {2}, {1}, {0}".format(*numbers))

name=input("What is your name?: ")
name_list = list(name)
print("The first letter of your name is {0}".format(*name_list))

names=["Conan", "Valeria", "Belt"]
ages=[25, 22, 32]
print("{0[0]} is {1[0]}, {0[1]} is {1[1]} and {0[2]} is {1[2]}".format(names,ages))