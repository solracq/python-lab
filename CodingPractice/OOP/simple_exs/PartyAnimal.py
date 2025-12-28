'''
@author: Solrac
'''
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, name):
        self.name = name
        
    def party(self):
        self.x += 1
        print(self.name, 'party count', self.x)
        
s = PartyAnimal("Sally")
j = PartyAnimal('Jim')
s.party()
j.party()
s.party()
s.party()

print(type(s))
print(type(j.party))
print(dir(PartyAnimal))