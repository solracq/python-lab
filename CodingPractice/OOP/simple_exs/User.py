'''
@author: Solrac
'''
class User():
    def __init__(self, first_name, last_name, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.location = location
    
    def describe_user(self):
        print(self.first_name, self.last_name, "has the email", self.email, "and lives at", self.location)
        
    def greeting_user(self):
        print("kiovo Sr/Sra", self.last_name,"!")