'''
@author: Solrac
'''
from Users import Users

class UserChild(Users):
    def __init__(self, first_name, last_name, age, hobby):
        super().__init__(first_name, last_name, age, hobby)
        self.favorite_movie = ""
    
    def get_user_movie(self):
        user = self.first_name +' what is your favorite movie?'
        self.favorite_movie = input(user)
        self.dict_user['movie'] = self.favorite_movie
        
    def show_updated_records(self):
        self.print_user_records()
        
user1 = UserChild('HT', 'Sm', 5, 'playing cars')
user1.create_user_records()
user1.get_user_movie()
user1.show_updated_records()
print()

user2 = UserChild('AB', 'Sm', 3, 'drawing princess')
user2.create_user_records()
user2.get_user_movie()
user2.show_updated_records()