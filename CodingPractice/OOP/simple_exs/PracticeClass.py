'''
@author: Solrac
'''
class PracticeClass:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print('I am constructed', self.x, self.y)
        
    def sum(self):
        print(self.x + self.y)
    
    def increase(self):
        self.x += 1
        print(self.x)
        
    def __del__(self):
        print('I am destructed', self.x, self.y)
        
       
pc = PracticeClass(8, 8)
pc.sum()
print()
pc.increase()
pc.increase()
pc.increase()
pc.increase()
print(pc.x)
print(pc.y)
PracticeClass.increase(pc)
print(type(pc.x))
print(type(pc.increase))
print(dir(pc))

pc1 = PracticeClass(1,1)
pc2 = PracticeClass(2,1)
pc3 = PracticeClass(33, 117)
pc1.sum()
pc2.sum()
pc3.sum()
pc1.increase()
pc2.increase()
pc3.increase()
