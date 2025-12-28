'''
@author: Solrac
'''
import logging

logging.debug("Start Program")
def urlify(s):
    s = s.strip()
    alist = list(s)
    newlist = []
    
    for i in range(len(alist)):
        if alist[i] == ' ':
            newlist.append("%20")
        else:
            newlist.append(alist[i])
    
    logging.debug("Converting to string")
    new_string = "".join(newlist)
    
    return new_string
logging.debug("End of Program")

def improvedurlify(s):
    s = s.strip()
    print(s.replace(" ", "%20", 2))
            

s = "  Mr. John Smith "
print(s)
#print(urlify(s))
print(improvedurlify(s))

newlista = []
lista = ["Crear", "algo", "para", "que", "trabaje"]
for i in range(len(lista)-1, -1, -1):
    newlista.append(lista[i])
newlista = " ".join(newlista)   
print(newlista)
