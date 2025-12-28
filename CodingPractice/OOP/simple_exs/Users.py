'''
@author: Solrac
'''

""" A class that can be used to represent a user record"""

class Users():
    def __init__(self, first_name, last_name, age, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
        self.dict_user = {}
        self.login_attempts = 0
        
    def create_user_records(self):
        self.dict_user = {'first_name': self.first_name, 'last_name': self.last_name, 'age': self.age, 'hobby': self.hobby}
        return self.dict_user
    
    def print_user_records(self):
        for key, value in self.dict_user.items():
            print('{} : {}'.format(key, value))
            
    def greet_user(self):
        question = 'Hello ' + self.first_name + " " + self.last_name +' would you like ' + self.hobby +'? '
        answer = input(question)
        if answer.lower() == 'yes' or answer.lower() == 'y':
            print('Great, lets', self.hobby)
        else:
            print('Its OK, we can read books then!')
            
    def get_future_age(self):
        print(self.first_name, self.last_name, 'next year you will be', self.age + 1)
        
    def print_login_attempts(self):
        print(self.login_attempts)
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
            
user1 = Users('C', 'Tz', 5, 'playing cars')
user1.create_user_records()
user1.print_user_records()
user1.get_future_age()
user1.greet_user()
user1.print_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.print_login_attempts()
user1.reset_login_attempts()
user1.print_login_attempts()
print()

