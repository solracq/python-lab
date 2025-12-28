'''
@author: Solrac
'''
from PracticeClass import PracticeClass

class PracticeChildClass(PracticeClass):
    points = 0
    
    def six(self):
        self.points += 6
        self.increase()
        print(self.x, self.y, 'points', self.points)

class childPC(PracticeClass):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
        self.result = 0
        
    def multiplyResults(self):
        return self.x * self.y * self.z
    
    def incr(self):
        self.increase()
        self.y += 1
        self.result = self.x + self.y + self.z
        return self.result

s = PracticeClass(7, 8)
s.sum
s.increase()
j = PracticeChildClass(9, 1)
j.increase()
j.six()
print(dir(j))        

cpc = childPC(2, 4, 6)
print(cpc.multiplyResults())
print("Before", cpc.result)
print("After", cpc.incr(), "where", " x= ", cpc.x, ' y= ', cpc.y, ' z= ', cpc.z)