'''
@author: Solrac
'''

class User2():
    def __init__(self, name, lastname, username, email, voter):
        self.name = name
        self.lastname = lastname
        self.username = username
        self.email = email
        self.voter = voter
        self.dict = dict
        
    def set_name(self, name):
        self.name = name
    
    def set_lastname(self, lastname):
        self.lastname = lastname
        
    def set_username(self, username):
        self.username = username
    
    def set_email(self, email):
        self.email = email
    
    def set_voter(self, voter):
        self.voter = voter
        
    def get_name(self):
        return self.name
    
    def get_lastname(self):
        return self.lastname
    
    def get_username(self):
        return self.username
    
    def get_email(self):
        return self.email
    
    def get_voter(self):
        return self.voter
    
    def get_fullname(self):
        return self.name+" "+self.lastname
    
    def create_dictionary(self, dictionary, name, lastname, username, email, voter):
        #dict= {}
        dictionary[username]= {
                            'name': name.title(),
                            'lastname': lastname.title(),
                            'email': email,
                            'voter': voter,
                        }
        
        for keys, values in dictionary.items():
            print("{}: ".format(keys))
            for key, value in values.items():
                print("\t{}: {}".format(key, value))

class UserChild(User2):
        def __init__(self, name, lastname, username, email, voter):
            super().__init__(name, lastname, username, email, voter)
            self.location = "Canada"
        
        def get_location(self):
            return self.location
        