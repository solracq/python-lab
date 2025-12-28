'''
@author: Solrac
'''
import sys
from sys import argv

name = sys.argv[1] 
subject = sys.argv[2]
hobbie = sys.argv[3]
print("My name is", name)
print("I'm studying", subject)
if sys.argv[2] == 'python':
    print("good for you!")
print("my hobbie is", hobbie)
