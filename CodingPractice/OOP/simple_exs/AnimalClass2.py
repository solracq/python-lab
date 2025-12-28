'''
@author: Solrac
'''

class Animal2:
    def __init__(self, name, type, skill, food):
        self.name = name
        self.type = type
        self.skill = skill
        self.food = food
        self.speed = 0
        
    def set_name(self, name):
        if name == str(name):
            self.name = name
        else:
            raise Exception('Invalid input! Please use strings')
        
    def set_type(self, type):
        if type == str(type):
            self.type = type
        else:
            raise Exception('Invalid input! Please use strings')
        
    def set_skill(self, skill):
        if skill == str(skill):
            self.skill = skill
        else:
            raise Exception('Invalid input! Please use strings')
        
    def set_food(self, food):
        if type(food) == str:
            self.food = food
        else:
            raise Exception('Invalid input! Please use strings')
    
    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.type
    
    def get_skill(self):
        return self.skill
    
    def get_food(self):
        return self.food
    
    def set_speed(self, speed):
        if type(speed) == int:
            self.speed = speed
        else:
            raise Exception('Invalid input! Please use strings')
        
    def print_animal_data(self):
        print("{} is of type {} with skill {} and with speed of {}km/h. The {} eats {}.".
              format(self.name, self.type, self.skill, self.speed, self.name, self.food))
        
    def increase_speed(self, speed):
        self.speed += speed
        
    def show_speed(self):
        print("The initial speed of {} is {}".format(self.name, self.speed))