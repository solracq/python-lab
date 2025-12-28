'''
@author: Solrac
'''
from CodingPractice.OOP.simple_exs.PartyAnimal import PartyAnimal

class CricketFan(PartyAnimal):
    pts = 0
    
    def six(self):
        self.pts += 6
        self.party()
        print(self.name, "points", self.pts)
        
s = PartyAnimal('Sally')
s.party()
j = CricketFan('Jim')
j.party()
j.six()
j.six()
s = CricketFan('Sally')
s.six()
print(dir(CricketFan))