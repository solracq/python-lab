'''
@author: Solrac
'''
from CodingPractice.OOP.simple_exs.Users import Users
from Privileges import Privileges

class Admin(Users):
    def __init__(self, first_name, last_name, age, hobby):
        super().__init__(first_name, last_name, age, hobby)
        self.privileges = Privileges()
            
print()
admin = Admin('CarlitoS', 'Q.', 5, 'read superheroes books')
admin.create_user_records()
admin.print_user_records()
admin.privileges.show_privileges()
print(admin.privileges.prvileges)