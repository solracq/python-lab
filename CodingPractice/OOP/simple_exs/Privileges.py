'''
@author: Solrac
'''
class Privileges():
    def __init__(self):
        self.prvileges = ['can add post', 'can delete post', 'can ban user']
        
    def show_privileges(self):
        print('Admin privilages:')
        for privilege in self.prvileges:
            print(privilege)