'''
@author: Solrac
'''
list_=['a', 'b', 'c', 'd', 'e', 'f']
if 'c' in list_:
    print("{} in list".format(list_[2]))

if 'k' not in list_:
    print("k not in list")
   
a=5
b=3
c=5 
if a != b:
    print("not equals")
    
if not(a == b):
    print("not equals")
    
status= False
if (a==b) and (a==c):
    status = True
else:
    status = False
print(status)

if (a==b) or (a==c):
    status=True
else:
    status=False
print(status)

list_=[5,2]
if list_:
    for element in list_:
        print(element)
else:
    print("list is empty!")    
  
list_ = ["admin", "developer", "moderator", "guest"]  
if list_:
    for user in list_:
        if (user == "admin") and (user in list_):
            print("admin has full privileges")
        if (user == "developer") and (user in list_):
            print("developer has almost full privilages")
        if (user == "moderator") and (user in list_):
            print("moderator has more privileges than dev")
        if (user== "guest") and (user in list_):
            print("guest has minimal permissions")
else:
    print("list is empty")
print()

current_users=["voldo", "valeria", "conan", "CAPITAN_CRUNCH", "warrior"]
new_users=["rocky", "voldo", "sub=zero", "valeria", "gunter"]

for user in new_users:
    if user in current_users:
        print(user+" username has been taken, choose another one")
        name=input().lower()
        new_users.remove(user)
        new_users.append(name)
    else:
        print(user+" is a new user and it will be added later to the list of current users")
new_list= current_users+new_users        
print("current users", current_users)
print("new users", new_users)
print("New list", new_list)
print()

list_ = [i for i in range(1, 11)]
print(list_)
if list_:
    for i in list_:
        if i == 1:
            print("1st")
        elif i == 2:
            print("2nd")
        elif i == 3:
            print("3rd")
        elif i == 4:
            print("4th")
        elif i == 5:
            print("5th")
        elif i == 6:
            print("6th")
        elif i == 7:
            print("7th")
        elif i == 8:
            print("8th")
        elif i == 9:
            print("9th")
        elif i == 10:
            print("10th")
else:
    print("list is empty")
            