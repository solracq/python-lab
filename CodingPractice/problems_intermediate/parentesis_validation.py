'''
@author: Solrac
'''

def parentesis_balancing(lista):
    op = ['(', '{', '[']
    cp = [')', '}', ']']
    stack = []
    
    for i in range(len(lista)):
        if lista[i] in op:
            stack.append(lista[i])
        elif lista[i] in cp:
            location = cp.index(lista[i])
            if (len(stack) > 0) and (op[location] == stack[len(stack)-1]):
                stack.pop()
            else:
                return "UNBALANCED"
    if len(stack) == 0:
        return "BALANCED"
    

lista = ['{', '(', ')', '[', ']', '}']
print(lista)
print(parentesis_balancing(lista))