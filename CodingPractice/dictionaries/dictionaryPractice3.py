'''
@author: Solrac
'''

def create_account(dictionary, username, name, lastname, age, email, location, interest, language, profession, voter):
    '''username = input("username: ")
    name = input('name: ')
    lastname = input('last name: ')
    age = input('age: ')
    email = input('email: ')
    location = input('location: ')
    interest = input('interest: ')
    language = input('language: ')
    profession = input('profession: ')
    voter = input('voter')'''
    
    dictionary[username]= {
                           'name': name.capitalize(),
                           'lastname': lastname.capitalize(),
                           'age': int(age),
                           'email': email.lower(),
                           'location': location.capitalize(),
                           'interest': interest.title(),
                           'language': language.capitalize(),
                           'profession': profession.title(),
                           'voter': voter,
                           }
    
    return dictionary

def print_dictionary(dictionary):
    for username, userinfo in dictionary.items():
        print("{}".format(username))
        print("\tname:{}".format(userinfo['name']+" "+userinfo['lastname']))
        print("\tage:{}".format(userinfo['age']))
        print("\temail:{}".format(userinfo['email']))
        print("\tlocation:{}".format(userinfo['location']))
        print("\tinterest:{}".format(userinfo['interest']))
        print("\tlangage:{}".format(userinfo['language']))
        print("\tprofession:{}".format(userinfo['profession']))
        print("\tvoter:{}".format(userinfo['voter']))
        
def find_user_info(dictionary, username, userinfo=None):
    print("Fond the following user: ")
    if userinfo == None:
        for user, information in dictionary.items():
            if user == username:
                print("{}: ".format(user))
                for key, value in information.items():
                    print("\t{}:  {}".format(key, value))
    else:
        for user, information in dictionary.items():
            if user == username:
                print("{}: ".format(user))
                for key, value in information.items():
                    if key == userinfo:
                        print("{} : {}".format(key, information[key]))
        
        
dict = {}
account1 = create_account(dict, 'cquiroz', 'carlos', 'quiroz', 40, 'car@loquesea.com', 'canada', 'movies', 'java', 'qa', True)
account2 = create_account(dict, 'yzhang', 'yu', 'zhang', 34, 'yu@loquesea.com', 'canada', 'music', 'python', 'account', True)
account3 = create_account(dict, 'caloEddy', 'carlitos', 'quroz', 4, 'cquirEdy@loquesea.com', 'canada', 'dragons', 'scratch', 'engineer', False)
account4 = create_account(dict, 'nquiroz', 'naomi', 'quroz', 2, 'nquiroz@loquesea.com', 'canada', 'princess', 'scratch', 'engineer', False)
print_dictionary(dict)

print("Looking for an user: ")
find_user_info(dict, "yzhang", None)
print()

print("Looking for a prticular user info: ")
find_user_info(dict, "nquiroz", "interest")

print()
find_user_info(dict, "caloEddy")

# copying a list as argument
list_ = ['a', 'b', 'c', 'd', 'e']
def print_list(list_name):
    removed = list_name.pop(2)
    print("removed", removed)
    print(list_name)
print(list_)
print_list(list_[:])
print(list_,"\n")

# passing multiple arguments of unknown Number
def print_(*elements):
    print(elements)
print_('f')
print_('g', 'h')
print_('i', 'k', 'm', 1, 2, 3, 4, 5)
