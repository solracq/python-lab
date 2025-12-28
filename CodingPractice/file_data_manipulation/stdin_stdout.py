'''
@author: Solrac
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

4
"bcdef"
"abcdefg"
"bcde"
"bcdef"

n = int(sys.stdin.readline())
#next_line = str(sys.stdin.readline())j
list_ = []

while n > 0:
    list_.append(sys.stdin.readline().split())
    n -= 1

print(list_)
#OUTPUT:
# [['bcdef'], ['abcdefg'], ['bcde'], ['bcdef']]

################################################################

n = int(sys.stdin.readline())
list_ = []

while n > 0:
    list_.append(str(sys.stdin.readline()).strip('\n'))
    n -= 1

print(list_)
      
#OUTPUT:
# ['bcdef', 'abcdefg', 'bcde', 'bcdef']

#########################################################################
5
"Harry"
37.21
"Berry"
37.21
"Tina"
37.2
"Akriti"
41
"Harsh"
39

if __name__ == '__main__':
    list_ = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista = [name, score]
        list_.append(lista)

    print(list_)
    
#OUTPUT
# [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]

###############################################################################################
4
'a a c d'
2

n = int(sys.stdin.readline())

list_ = []

list_=sys.stdin.readline().split()

k = int(sys.stdin.readline())

print(n)
print(list_)
print(k)

#OUTPUT
#4
#['a', 'a', 'c', 'd']
#2

