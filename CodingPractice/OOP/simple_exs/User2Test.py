'''
@author: Solrac
'''
import User2
import User3

def test_user2(name, lastname, username, email, voter):
    my_user2 = User2.User2(name, lastname, username, email, voter)
    
    print("Print class vars (attributes): {}, {}, {}, {}, {}".format(my_user2.name, my_user2.lastname, my_user2.username, my_user2.email, my_user2.voter))
    my_user2.set_name("A")
    my_user2.set_email("a@loquesea.com")
    my_user2.set_voter(False)
    print("Print class vars (attributes): {}, {}, {}, {}, {}".format(my_user2.name, my_user2.lastname, my_user2.username, my_user2.email, my_user2.voter))
    print(my_user2.get_fullname())
    dictionary = {}
    my_user2.create_dictionary(dictionary, name, lastname, username, email, voter)
    
    my_user3 = User3.UserChild(name, lastname, username, email, voter)
    print(my_user3.get_location())
    dictionary2 = {}
    my_user3.create_dictionary(dictionary2, name, lastname, username, email, voter)

test_user2("t", "r", "o", "tr@loquesea.com", True)
test_user2("a", "g", "h", "ag@loquesea.com", True)