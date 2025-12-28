'''
@author: Solrac
'''

class animal():
    def __init__(self, name, types, skill, food):
        self.name = name
        self.types = types
        self.skill = skill
        self.food = food
        self.speed = 0
        
    def set_name(self, name):
        if name == str(name):
            self.name = name
        else:
            raise Exception('Invalid input! Please use strings')
    
    def set_type(self, types):
        if types == str(types):
            self.types = types
        else:
            raise Exception('Invalid input! Please use strings')
        
    def set_skill(self, skill):
        if skill == str(skill):
            self.skill = skill
        else:
            raise Exception('Invalid input! Please use strings')
        
    def set_food(self, food):
        if food == str(food):
            self.food = food
        else:
            raise Exception('Invalid input! Please use strings')
    
    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.types
    
    def get_skill(self):
        return self.skill
    
    def get_food(self):
        return self.food
    
    def set_speed(self, speed):
        if speed == int(speed):
            self.speed = speed
        else:
            raise Exception('Invalid input! Please use integers')
        
    def print_animal_data(self):
        print("{} is of type {} with skill {} and with speed of {}km/h. The {} eats {}.".format(self.name, self.types, self.skill, self.speed, self.name, self.food))
    
    def increase_speed(self):
        self.speed += 10
        
    def show_speed(self):
        print("The initial speed of {} is {}".format(self.name, self.speed))